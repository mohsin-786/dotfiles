resource "aws_vpc" "vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "VPC"
  }
}
resource "aws_subnet" "subnet" {
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = var.az
  map_public_ip_on_launch = true
  tags = {
    Name = "Subnet"
  }
}
resource "aws_internet_gateway" "gateway" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    Name = "Gateway"
  }
}
resource "aws_route_table" "route" {
  vpc_id = aws_vpc.vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gateway.id
  }
  tags = {
    Name = "route-table"
  }
}
resource "aws_route_table_association" "table_associate" {
  subnet_id      = aws_subnet.subnet.id
  route_table_id = aws_route_table.route.id

}
resource "aws_security_group" "sec-group" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.vpc.id

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "sec-group"
  }
}
resource "aws_network_interface" "eni" {
  subnet_id       = aws_subnet.subnet.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.sec-group.id]
}
resource "aws_eip" "eip" {
  vpc                       = true
  network_interface         = aws_network_interface.eni.id
  associate_with_private_ip = "10.0.1.50"
  instance                  = aws_instance.ubuntu.id
  depends_on = [
    aws_internet_gateway.gateway,
    aws_instance.ubuntu
  ]
}
resource "aws_key_pair" "ssh" {
  key_name   = var.key
  public_key = file("~/.ssh/id_rsa.pub")
}
resource "aws_instance" "ubuntu" {
  ami               = "ami-0b828c1c5ac3f13ee"
  instance_type     = "t2.micro"
  availability_zone = var.az
  key_name          = var.key
  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.eni.id
  }
  user_data = <<-EOF
        #! /bin/bash
        sudo apt update -y
        sudo apt install nginx -y
        sudo systemctl start nginx.service
        sudo bash -c 'echo Terraform is Great > /var/www/html/index.html'
        EOF
  tags = {
    "Name" = "web-server"
  }
}
output "ip" {
  value = aws_eip.eip.public_ip
}

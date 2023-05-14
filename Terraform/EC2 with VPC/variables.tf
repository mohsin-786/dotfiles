variable "az" {
  type    = string
  default = "ap-northeast-1a"
}
variable "key" {
  type    = string
  default = "sinkey"
}
variable "num" {
  type = set(number)
  default = [100, 200, 5, 4, 8]
}

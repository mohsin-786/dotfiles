for images in $(ls images)
do
        if [[ $images = *.jpeg ]]
        then
                new=$(echo $images | sed 's/jpeg/jpg/g')
                mv images/$i images/$new
        fi
done

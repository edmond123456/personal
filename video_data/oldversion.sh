#!/usr/bin/bash                 
#!/usr/bin/python

read -p "please input address of the video files: "  ip_video  #  /Users/junjie_hua/personal/video_data
read -p "please input name of the video files: "  name_video  #  video.mp4
read -p "please input address where you want to save: "  ip_save #  /Users/junjie_hua/personal/video_data
cd $ip_save
#pwd
rm -rf test
mkdir test
#ls

cd $ip_video
cp -R $name_video /Users/junjie_hua/personal/video_data/test/1.mp4
cd test

ffmpeg -i 1.mp4 -f image2 -vf fps=fps=3 data%d.png
#ls /Users/junjie_hua/personal/video_data/test

#convert +append data1.png data2.png data3.png  1.png

num=0
add=1
for file in *.png
    do num=$[$num+$add]
done
echo "We have $num png files."


int=1
add_1=1
add_2=2
devide=3
while(($int<=$[$num / $devide]))
do
  convert +append "data"$[$int*3-$add_2]".png" "data"$[$int*3-$add_1]".png" "data"$[$int*3]".png" ""$int".jpg"
  let "int++"
done


echo TRANSFORM DONE!

rm 1.mp4
for file in *.png
    do rm "$file"
done

echo DELETE DONE!

#ffmpeg -i input.jpg -vf scale=320:240 output_320x240.png

for file in *.jpg
    do ffmpeg -i "$file" -vf scale=416:128 "${file%*.jpg}"
done
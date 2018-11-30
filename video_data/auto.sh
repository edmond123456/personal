#!/usr/bin/bash                 
#!/usr/bin/python

ip_video=/Users/junjie_hua/personal/video_data
name_video=video.mp4
ip_save=/Users/junjie_hua/personal/video_data
fps_fig=3


#echo ip_video
#echo name_video
#echo ip_save
#echo $fps_fig

cd $ip_save
#pwd
rm -rf test
mkdir test
#ls

cd $ip_video
cp -R $name_video /Users/junjie_hua/personal/video_data/test/1.mp4
cd test

ffmpeg -i 1.mp4  -vf scale=416:128 2.mp4
echo "Reesize done"

ffmpeg -i 2.mp4 -f image2 -vf fps=fps=$fps_fig data%d.png
#ls /Users/junjie_hua/personal/video_data/test

#convert +append data1.png data2.png data3.png  1.png


#ffmpeg -i input.jpg -vf scale=320:240 output_320x240.png

num=0
add=1
for file in *.png
    do num=$[$num+$add]
done




int=1
add_1=1
add_2=2
devide=3
while(($int<=$[$num-$add_2]))
do
  convert +append "data"$[$int]".png" "data"$[$int+$add_1]".png" "data"$[$int+$add_2]".png" ""$int".jpg"
  let "int++"
done

num=0
add=1
for file in *.jpg
    do num=$[$num+$add]
done
echo "We have $num jpg files."

for file in *.mp4
    do rm "$file"
done
for file in *.png
    do rm "$file"
done
echo DELETE DONE!
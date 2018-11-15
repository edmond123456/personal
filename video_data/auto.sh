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

ffmpeg -i 1.mp4 -f image2 -vf fps=fps=1/10 data%d.png
#ls /Users/junjie_hua/personal/video_data/test

#convert +append data1.png data2.png data3.png  1.png

num=0
add=1
for file in *.png
    do num=$[$num+$add]
done
echo "$num png files have been transformed."

echo OK!
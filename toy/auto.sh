#!/usr/bin/bash                 
#!/usr/bin/python

cd /Users/junjie_hua/personal/video_data
rm -rf test
mkdir test
ls

cp -R video.mp4  /Users/junjie_hua/personal/video_data/test/1.mp4
cd test

ffmpeg -i 1.mp4 -f image2 -vf fps=fps=1/20 data%d.png
#ls /Users/junjie_hua/personal/video_data/test

convert +append data1.png data2.png data3.png  1.png










#echo OK!
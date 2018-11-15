#!/usr/bin/bash                 
#!/usr/bin/python


cd /Users/junjie_hua/personal/video_data/test

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
  convert +append "data"$[$int*3-$add_2]".png" "data"$[$int*3-$add_1]".png" "data"$[$int*3]".png" ""$int".png"
  let "int++"
done


echo DONE!




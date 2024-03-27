#!/bin/bash


args=(51 52 53 54 55 56 57 58 59 60)

mkdir see_ed_result

for i in ${args[@]}  #i traverse 遍历
do 
    python3 driver.py -arg1 $i > see_ed_result/$i.part
done


#wait
#cd see_ed_result
#cat *.part > df_ed.csv #每次都要改！
#rm *.part

cd ..


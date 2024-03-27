#!/bin/bash


args=(61 62 63 64 65 66 67 68 69 70)

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


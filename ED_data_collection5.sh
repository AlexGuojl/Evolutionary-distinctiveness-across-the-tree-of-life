#!/bin/bash


args=(41 42 43 44 45 46 47 48 49 50)

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


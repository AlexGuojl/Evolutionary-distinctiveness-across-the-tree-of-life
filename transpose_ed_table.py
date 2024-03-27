#transpose df_ed.csv
import os
import pandas as pd
os.chdir("/Users/alexgjl/Desktop/try_python_shell/see_ed_result")
df_ed  = pd.read_csv("df_ed.csv",low_memory=False,header = None)
df_ed = df_ed.transpose()
df_ed0 = df_ed
df_ed["ed"] = df_ed0.median(axis=1)
df_ed["sum_ed"] = list(df_ed0.apply(lambda x: x.sum(), axis = 1))
leaves2 = leaves1
leaves2['id'] = leaves2['id'].astype(str)
leaves2 = leaves2.groupby("parent")["id"].apply(lambda x:x.str.cat(sep = ",")).reset_index()
df_ed["parent"]=leaves2["parent"]
leaves_with_ed = pd.merge(leaves1,df_ed,how = "left",on = "parent")
df_median_ed = pd.DataFrame(df_ed,columns = ["id","parent","ed"])

df_median_ed.to_csv("median_ed_final.csv",encoding = "gbk")
df_ed.to_csv("bootstraped_ed(1_100).csv",encoding = "gbk")

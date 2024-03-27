#transpose df_ed.csv
import os
import pandas as pd
os.chdir("/Users/alexgjl/Desktop/try_python_shell/see_ed_result")
df_ed  = pd.read_csv("df_ed.csv",low_memory=False,header = None)
df_ed1 = df_ed.transpose()
df_ed1.to_csv("ed_bootstrap(100).csv",encoding = "gbk")

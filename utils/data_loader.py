import pandas as pd
import glob

def load_multiple_csv(folder_path):
    files = glob.glob(folder_path + "/*.csv")
    df_list = [pd.read_csv(file) for file in files]
    return pd.concat(df_list, ignore_index=True)

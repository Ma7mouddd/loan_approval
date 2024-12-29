import sys
import pandas as pd
import os
import io



def load_dataset(file):
    df = pd.read_csv(file)
    print("Data loaded successfully.")
    print(df.head())
    with open("./output/data/head.txt", "w") as f:
        f.write(df.head().to_string())
        
    df.to_csv("loaded.csv", index=False)
    print("Data saved to loaded.csv")

if __name__ == "__main__":
    file_path = './loan_data.csv'
    load_dataset(file_path)
    os.system("python eda.py")
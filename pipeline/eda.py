import pandas as pd
import os

def eda(file):
    # Load the dataset
    df = pd.read_csv(file)

    # 1. Save DataFrame information
    with open("./output/eda/eda-in-1.txt", "w") as f:
        f.write("DataFrame Information\n")
        df.info(buf=f)

    # 2. Save summary statistics of numeric columns
    with open("./output/eda/eda-in-2.txt", "w") as f:
        f.write("Summary Statistics of Numeric Columns\n")
        f.write(df.describe().to_string())
    
    
    # 3. Save correlation matrix of numeric columns
    numeric_df = df.select_dtypes(include=['number'])  # Filter numeric columns
    correlation_matrix = numeric_df.corr().to_string()
    with open("./output/eda/eda-in-3.txt", "w") as f:
        f.write("Correlation Matrix of Numeric Columns\n")
        f.write(correlation_matrix)

    # 4. Identify categorical and numerical columns
    cat_cols = [var for var in df.columns if df[var].dtypes == 'object']
    num_cols = [var for var in df.columns if df[var].dtypes != 'object']

    # Print the lists to the console
    print(f'Categorical columns: {cat_cols}')
    print(f'Numerical columns: {num_cols}')

    # Save the lists to a file
    with open("./output/eda/eda-in-4.txt", "w") as f:
        f.write("Categorical Columns:\n")
        f.write(", ".join(cat_cols) + "\n\n")
        f.write("Numerical Columns:\n")
        f.write(", ".join(num_cols))

    print("EDA completed.")

if __name__ == "__main__":
    eda("loaded.csv")
    os.system("python vis.py")

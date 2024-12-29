import pandas as pd
import matplotlib.pyplot as plt
import os


def visualization(input_file):
    # Load the processed dataset
    df = pd.read_csv(input_file)

    # 1. Bar chart of loan intent counts
    if 'loan_intent' in df.columns:
        df['loan_intent'].value_counts().plot(kind='bar', color='skyblue')
        plt.title('Loan Intent Counts')
        plt.xlabel('Loan Intent')
        plt.ylabel('Count')
        plt.savefig('./output/vis/loan_intent_counts.png')
        plt.close()

    # 2. Histogram of age distribution
    if 'person_age' in df.columns:
        df['person_age'].hist(color='orange', bins=20)
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig('./output/vis/age_distribution.png')
        plt.close()

    # 3. Boxplot for income
    if 'person_income' in df.columns:
        df.boxplot(column=['person_income'], vert=False)
        plt.title('Income Boxplot')
        plt.xlabel('Income')
        plt.savefig('./output/vis/income_boxplot.png')
        plt.close()

    print("Visualizations generated.")

if __name__ == "__main__":
    visualization("loaded.csv")
    os.system("python dpre.py")
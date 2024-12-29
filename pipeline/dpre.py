import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocess_data(input_file, output_file):
    try:
        # Load the dataset
        df = pd.read_csv(input_file)
        
        # 1. Data Cleaning
        df = df.dropna()  # Drop missing values
        df = df.drop_duplicates()  # Drop duplicate rows
        
        # 2. Data Scaling
        scaler = MinMaxScaler()
        if 'loan_amnt' in df.columns and 'person_income' in df.columns:
            df[['loan_amnt', 'person_income']] = scaler.fit_transform(df[['loan_amnt', 'person_income']])
        
        # 3. Label Encoding
        le = LabelEncoder()
        label_columns = [
            'previous_loan_defaults_on_file', 
            'loan_intent', 
            'person_home_ownership', 
            'person_education', 
            'person_gender'
        ]
        for col in label_columns:
            if col in df.columns:
                df[col] = le.fit_transform(df[col])
        
        # 4. Age Conversion and Filtering
        if 'person_age' in df.columns:
            df['person_age'] = df['person_age'].astype('int')
            df = df.loc[~(df['person_age'] > 70)]
        
        # Save the processed data
        df.to_csv(output_file, index=False)
        print(f"Data preprocessing complete. Processed file saved as {output_file}")
        print("Preprocessing step executed successfully.")
    
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        raise

if __name__ == "__main__":
    preprocess_data("loaded.csv", "res_dpre.csv")
    print("preprocessing is done")
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def decision_tree_tuning_and_evaluation(input_file, output_file, confusion_matrix_file):
    # Load the dataset
    df = pd.read_csv(input_file)

    # Separate features (X) and target (y)
    X = df.drop('loan_status', axis=1)
    y = df['loan_status']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Decision Tree classifier
    dt_classifier = DecisionTreeClassifier(random_state=42)

    # Define the hyperparameter grid
    param_grid = {
        'max_depth': [3, 5, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'criterion': ['gini', 'entropy']
    }

    # Perform GridSearchCV to find the best hyperparameters
    grid_search = GridSearchCV(
        estimator=dt_classifier,
        param_grid=param_grid,
        scoring='roc_auc',  # Use ROC-AUC as the evaluation metric
        cv=5,              # 5-fold cross-validation
        verbose=1,
        n_jobs=-1
    )

    # Fit the GridSearchCV
    grid_search.fit(X_train, y_train)

    # Extract the best model
    best_dt_model = grid_search.best_estimator_

    # Evaluate the model on the test set
    y_pred = best_dt_model.predict(X_test)
    roc_auc = roc_auc_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    # Save the results to the output file
    with open(output_file, 'w') as f:
        # Write hyperparameter tuning results
        f.write("Best Hyperparameters:\n")
        for param, value in grid_search.best_params_.items():
            f.write(f"{param}: {value}\n")
        f.write(f"\nBest ROC-AUC Score during cross-validation: {grid_search.best_score_}\n\n")

        # Write evaluation metrics
        f.write("Test Set Evaluation Metrics:\n")
        f.write(f"ROC-AUC Score: {roc_auc}\n")
        f.write("\nClassification Report:\n")
        f.write(report)

    # Plot and save the confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Rejected', 'Approved'],
                yticklabels=['Rejected', 'Approved'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.savefig(confusion_matrix_file)
    plt.close()

    print("Decision Tree hyperparameter tuning and evaluation is complete.")

if __name__ == "__main__":
    # Example usage
    decision_tree_tuning_and_evaluation(
        input_file="./output/final.csv",
        output_file="./output/model_output/k.txt",
        confusion_matrix_file="./output/model_output/confusion_matrix.png"
    )

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import numpy as np

def sort_dataset(data_df):

    return data_df.sort_values(by='year', ascending=True)


# TODO: Implement this function

def split_dataset(data_df):

    Y = data_df['salary'] * 0.001
    X = data_df.drop('salary', axis=1)
    X_train = X.iloc[:1718]
    X_test = X.iloc[1718:]
    Y_train = Y.iloc[:1718]
    Y_test = Y.iloc[1718:]

    return X_train, X_test, Y_train, Y_test


# TODO: Implement this function

def extract_numerical_cols(data_df):
    numerical_cols = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI',
                      'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
    return data_df[numerical_cols]


# TODO: Implement this function

def train_predict_decision_tree(X_train, Y_train, X_test):
    model = DecisionTreeRegressor()
    model.fit(X_train, Y_train)
    return model.predict(X_test)

# TODO: Implement this function

def train_predict_random_forest(X_train, Y_train, X_test):
    model = RandomForestRegressor()
    model.fit(X_train, Y_train)
    return model.predict(X_test)


# TODO: Implement this function

def train_predict_svm(X_train, Y_train, X_test):
    model = SVR()
    model.fit(X_train, Y_train)
    return model.predict(X_test)

# TODO: Implement this function

def calculate_RMSE(labels, predictions):
    return np.sqrt(mean_squared_error(labels, predictions))

# TODO: Implement this function

if __name__ == '__main__':
    # DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('/Users/junsu/Desktop/oss과제 2/2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
    print("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
    print("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
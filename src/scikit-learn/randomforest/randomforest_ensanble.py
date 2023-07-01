import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


if __name__ == "__main__":
    train_data_loc = r"data/train.csv"
    test_data_loc = r"data/test.csv"

    train_data = pd.read_csv(train_data_loc)
    # print(train_data.head())

    test_data = pd.read_csv(test_data_loc)
    # print(test_data.head())

    y = train_data["Survived"]
    # print(y.head())

    features = ["Pclass", "Sex", "SibSp", "Parch"]
    X = pd.get_dummies(train_data[features])
    # print(train_data[features].head())
    # print(X.head())
    X_test = pd.get_dummies(test_data[features])
    # print(X_test.head())

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X, y)
    predictions = model.predict(X_test)

    output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
    print(output.head())
    output.to_csv('src/scikit-learn/randomforest/submission.csv', index=False)
    print("Your submission was successfully saved!")
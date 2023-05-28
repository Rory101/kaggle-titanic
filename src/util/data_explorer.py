import os

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd
import numpy as np


SCRIPT_DIR = os.path.dirname(__file__)

TRAIN_CSV = os.path.join(SCRIPT_DIR, "../../data/train.csv")
TEST_CSV = os.path.join(SCRIPT_DIR, "../../data/test.csv")

DATA_TYPE_MAP = {
    "Pclass": "categorical",
    "Name": "unique",
    "Sex": "categorical",
    "Age": "categorical",
    "SibSp": "count",
    "Parch": "count",
    "Ticket": "unique",
    "Fare": "unique",
    "Cabin": "unique",
    "Embarked": "categorical"
}

def load_training_data() -> pd.DataFrame:
    return pd.read_csv(TRAIN_CSV)


def load_test_data() -> pd.DataFrame:
    return pd.read_csv(TEST_CSV)


class Passenger:
    def __init__(self) -> None:
        self.id = -1
        self.title = ""
        self.name = ""
        self.surname = ""
        self.pclass = np.nan
        self.ticket = ""
        self.sex = ""
        self.age = np.nan
        self.fare = np.nan
        self.cabins = []
        self.embarked = ""
        self.parch = np.nan
        self.sibsp = np.nan
        self.survived = -1
    
    def __repr__(self) -> str:
        return f"Pasanger {self.id}"
    
    def populate(self, inp: pd.Series):
        for c in inp.keys():
            if c == "PassengerId":
                self.id = inp[c]
            elif c == "Survived":
                self.survived = inp[c]
            elif c == "Pclass":
                val = inp[c]
                self.pclass = val
            elif c == "Name":
                surname, name = inp[c].split(", ")
                self.surname = surname
                idx = name.find(". ")
                title = name[:idx]
                name = name[idx+2:]
                self.title = title
                self.name = name
            elif c == "Sex":
                self.sex = inp[c]
            elif c == "Age":
                self.age = inp[c]
            elif c == "SibSp":
                self.sibsp = inp[c]
            elif c == "Parch":
                self.parch = inp[c]
            elif c == "Ticket":
                self.ticket = inp[c]
            elif c == "Fare":
                self.fare = inp[c]
            elif c == "Cabin":
                if not isinstance(inp[c], str):
                    cabins = []
                else:
                    cabins = inp[c].split(" ")
                    if not isinstance(cabins, list):
                        cabins = list(cabins)
                self.cabins = cabins
            elif c == "Embarked":
                self.embarked = inp[c]




def show_scatter_plot(data: pd.DataFrame, x_label: str, y_label: str):
    x_data = data[x_label]
    y_data = data[y_label]


    mycmap = colors.ListedColormap(['red', 'green'])

    plt.figure()
    sc = plt.scatter(x_data, y_data, c=data['Survived'], cmap=mycmap)
    plt.colorbar(sc)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    df: pd.DataFrame = load_training_data()

    passengers = []
    for i, x in df.iterrows():
        p = Passenger()
        p.populate(x)
        passengers.append(p)

    title = [p.title for p in passengers]

    print(df.columns)

    show_scatter_plot(df, "Fare", "Embarked")

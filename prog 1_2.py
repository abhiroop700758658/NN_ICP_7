# Tune hyperparameter and make necessary addition to the baseline model to improve validation accuracy
# Provide logical description of which steps lead to improved response and what was its impact on architecture behavior
from sklearn.model selection import train test split, GridSearchcv from sklear. Linear model import Logisticegression from sklearn datasets import load iris from skleam preprocessing import StandardScaler from sklear, pipeline import make pipeline
ndarray: y
iris = load iris )
X, y = iris data, iris target
ndarray with shape (150,)
x train, x val, y-train, y val = train test split(x, y, test size=0.2, random state=42)
pipeline = make pipeline/Standardscaler ), LogisticRegression (max iter=1000))
param grid =
'logisticregression_C*: [0.001, 0.01, 0.1, 1, 10, 100],
grid search = Gridsearchc(pipeline, param grid, v=5)
grid_search.fit(x_train, y_train)
print("Best hyperparameters:", grid search. best param.)
val_accuracy = grid_search.score(x val, y val)
print ("Validation Accuracy:", val accuracy)

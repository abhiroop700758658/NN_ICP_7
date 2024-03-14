#Use dataset of your own choice and implement baseline models provided from sklearn. linear_model import LogisticRegression from sklearn. mstrien imment accumanu copre
from sklearn. (module) model selection
from sklearn.model selection import train test split from sklearn.preprocessing import StandardScaler
iris = load _iris()
X, y = iris.data, iris.target
x train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
x train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler. transform(X_test)
logistic model = LogisticRegression(max_iter=1000)
logistic model.fit(x_train _scaled, y_train)
y_pred = logistic model.predict(X test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print ("Accuracy of Logistic Regression:", accuracy)
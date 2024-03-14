# Apply modified architecture to your own selected dataset and train it.
import tensorflow as tf from tensorflow.keras.models import Sequential
from sklearn.model selection import train test split from sklearn.preprocessing import Standardscaler
iris = load iris()
x, y = iris.data, iris.target
x train, x test, y_train, y _test = train test split(x, y, test_size=0.2, random state=42)
scaler = StandardScaler()
X train_scaled = scaler. fit_transform(X_train)
x test_scaled = scaler. transform(X_test)
model = Sequential ([|
Dense(10, activation='relu', input_shape=(X_train_scaled.shape[1],)),
Dense(20, activation='relu'), Dense(10, activation='relu'),
Dense(3, activation='softmax')
model. compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) model. fit(X_train_scaled, y_train, epochs=50, batch_size=8, verbose=1, validation split=0.1)
loss, accuracy = model. evaluate(X_test_scaled, y_test, verbose=1)
print ("Accuracy of Modified Neural Network:", accuracy
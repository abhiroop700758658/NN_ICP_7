# Evaluate the model on the testing set
loss, accuracy = model.evaluate(X_test_scaled, _test, verbose=1)
print ("Accuracy on Testing Set:", accuracy)
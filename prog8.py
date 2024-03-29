# Training and testing Loss and accuracy plots in one plot using subplot command and history object
history = model. fit(x_train_scaled, y_train, epochs=50, batch_size=8, verbose=1, validation split=0.1)
import matplotlib.pyplot as plt plt. figure(figsize=(12, 5))
plt. subplot (1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss', color='blue") plt.plot(history.history['val_loss'], label='Validation Loss', color='orange")
plt.title('Training and Validation Loss') plt. xlabel ('Epoch')
plt.ylabel('Loss')
plt.legend ()
pit. subplot (1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy', color='blue") plt.plot(history history ['val accuracy'], label='Validation Accuracy', color='orange') plt.title('Training and Validation Accuracy') plt. xlabel ('Epoch' )
plt.ylabel ('Accuracy')
plt. legend()
plt.tight_layout()
plt. show()

import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from sklearn.model_selection import train_test_split

sample_count = 700
train_count = 600
valid_count = sample_count - train_count
feature_count = 30
num_classes = 25
batch_size=10
epochs = 1

poses = np.loadtxt('poses.csv', delimiter=',')
idx = np.random.permutation(sample_count)
poses_shuffled = []

for i in range(sample_count):
	poses_shuffled.append(poses[idx[i]])

Y = np.zeros([sample_count])
for i in range(0,sample_count):
	Y[i] = i/100

y_shuffled = []
for i in range(sample_count):
	y_shuffled.append(Y[idx[i]])


poses_shuffled = np.array(np.asarray(poses_shuffled))
y_shuffled =  np.array(np.asarray(y_shuffled))

print (poses_shuffled.shape)
print (y_shuffled.shape)

x_train, x_test, y_train, y_test = train_test_split(poses_shuffled, y_shuffled, test_size=0.2, random_state=1)
print (x_train.shape)
print (y_train.shape)


y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(30,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

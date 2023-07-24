# %%
from sklearn.datasets import load_digits

digits = load_digits()

# %%
import matplotlib.pyplot as plt

idx = 37
plt.imshow(digits['images'][idx], cmap=plt.cm.gray)

# %%
# We see a 9
digits['target'][idx]

# %%
# The images are a constructed of 8 on 8 images but the data is flattened out to vectors of 64
digits['images'].shape, digits['data'].shape 
# ((1797, 8, 8), (1797, 64))

# %%
# First we need to split and train the data but we'll need to do one extra step. 
# The target is one dimensional, with values from 0 to 9. You need to transform each value to an array with 10 elements.
# All of them 0 except the one with the digits. 
# Since this is a common task, Keras has the utility to do just that.
from tensorflow.keras.utils import to_categorical

to_categorical([0, 1, 2, 0, 1])

# We see now that we get the output as vectors of 3. 
# Each row has 3 elements: either 0, 1, or 2 and 1 only in the place for the right value.
# Our first category is 0, and the first out put row is, 1,0,0; the second is 1, and the second row is 0,1,0 
# %%
# So now x is y of data and y we're going to convert it to categorical 
X = digits['data']
y = to_categorical(digits['target'])

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3)

# %%
# Now we are going to build our model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Activation

in_dim = X.shape[1]
out_dim = y.shape[1]

model = Sequential()
model.add(Dense(128, input_shape=(in_dim,)))
model.add(Activation('relu'))
model.add(Dense(out_dim))
model.add(Activation('sigmoid'))
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'],
)

# Keras generated a TensorFlow model
# %%
model.fit(X_train, y_train, epochs=10)

# %%
# Evaluate is slightly different than the score method from scikitlearn, but roughly the same.
_, accuracy = model.evaluate(X_test, y_test)
accuracy

# %%
model.predict(X_test[:3]) # the first 3 arguments
# We get an array with probability for each number
# But this is not helpful for us

# %%
# So we are going to call argmax (we want the location of the biggest argument and axis=1, meaning we want to work on every row)
model.predict(X_test[:3]).argmax(axis=1)

# %%
y_test[:3].argmax(axis=1)

# %%
# we can save the model
model.save('digits.h5')
# %%
# And load it again and get the same results
from tensorflow.keras.models import load_model

model1 = load_model('digits.h5')
model1.predict(X_test[:3]).argmax(axis=1)

# %%

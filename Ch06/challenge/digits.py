# %%
from sklearn.datasets import load_digits

digits = load_digits()
X, y = digits['data'], digits['target']

# %%
import matplotlib.pyplot as plt

i = 353
print(y[i])
img = digits['images'][i]
plt.imshow(img, cmap='gray')

# %%
img.shape

# %%
X.shape

# %%

"""
Write a pipeline that will learn to predict digits.
It should reduce the number of features to 10 and use a KNeighborsClassifier.

Split the data to train and test, and answer:
- What is the score of the pipeline on the test data?
- What is the size (in kb) of the serialized pipeline?
"""


# %%
from sklearn.decomposition import PCA # to reduce the features
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

pipe = Pipeline([
    ('pca', PCA(n_components=10)), #to reduce the features from 64 to 10
    ('clf', KNeighborsClassifier()),
])


# %%
#Now split the data to testing and training
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
)

#And get the score of the pipeline on the test data:
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)


# %%
#To get the size of the data, we are going to use pickle:
import pickle
kb = 2**10

data = pickle.dumps(pipe) #this is returning the bytes instead of saving to a file
len(data)/kb

#It gives us about 154 kb

#import program
#fit the training data
#apply transformations to data
#train the model by importing an estimator
#create an instance of the model
#fit the training data to our model
#predictions: predict()
#evaluate how well the model performed by using the classification report and confusion matrix

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

#assign data to a variable
cancer= load_breast_cancer()

#assign inputs from data to X
X=cancer['data']

#assign outputs from data to y
y = cancer['target']

#test_train_split() splits the data in half and trains the neural network (getting the biases) with the x/y_train data and trains those biases with x/y_test
#X_train and y_train are used to 'train' the network by comparing the outputs from x_train to the outputs it's supposed to have (y_train), then it adjusts the weights based on the error of the outputs
#x_test is inputed after the network is trained and the outputs are supposed to match y_test
X_train, X_test, y_train, y_test = train_test_split(X,y)

#scale data so that all variables in X are in the same range (same units/magnitude)
    #stadardized to have a mean 0 and variance 1
    #allows the network to process it faster
    #makes every value have an equal weight on the network- distribution is normal
scaler = StandardScaler()

#create an equation that fits the scaled X data
scaler.fit(X_train)

#computes the mean and std deviaton for the xtrain and xtest data
X_train= scaler.transform(X_train)
X_test= scaler.transform(X_test)

#the number of neurons you want at each layer
#the number of values inputed is the number of layers you are choosing to focus on
#creates the model that allows us to train other data with
#MLP= Multi-Layer Perceptron model
mlp= MLPClassifier(hidden_layer_sizes=(30,30,30))
mlp.fit(X_train,y_train)

MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(28), learning_rate='invscaling',
       learning_rate_init=0.00001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1000,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)

#learning_rate='adaptive' gave a higher accuracy than 'constant' and 'invscaling'



#the predictions for outputs of xtest
predictions= mlp.predict(X_test)

#allows us to evaluate how the model performed
#shows predictions
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

#a list of weight matrices- weight matrix at index i is the weights between layer i and layer i+1
len(mlp.coefs_)
len(mlp.coefs_[0])

#a list of bias vectors- vector at index i is the bias values added to layer i+1
len(mlp.intercepts_[0])
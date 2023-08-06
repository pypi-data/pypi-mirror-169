from numpy import array, hstack
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D

class Pre_data():
    def prepare_data(self, in_1, in_2):
        # define input sequence
        in_seq1 = array(in_1)
        in_seq2 = array(in_2)
        out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
        # convert to [rows, columns] structure
        in_seq1 = in_seq1.reshape((len(in_seq1), 1))
        in_seq2 = in_seq2.reshape((len(in_seq2), 1))
        out_seq = out_seq.reshape((len(out_seq), 1))
        return hstack((in_seq1, in_seq2, out_seq))
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MLP_Model(Pre_data,metaclass=Singleton):
    model = Sequential()
    def __init__(self, epoch):
        self.epochs = epoch
 # using for univariate multistep


        
    def build(self,n_input,n_steps_out, X, y):
        X = X.reshape((X.shape[0],n_input))
        MLP_Model.model.add(Dense(100, activation='relu', input_dim=n_input))
        MLP_Model.model.add(Dense(n_steps_out))
        MLP_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
    def predict(self, pred,n_input):
        x_input = array(pred)
        x_input = x_input.reshape((1,n_input))
        yhat = MLP_Model.model.predict(x_input, verbose=0)
        return yhat



class CNN_Model(Pre_data,metaclass=Singleton):

    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch
    

    def build(self, n_steps_in,n_steps_out,n_features,X,y):
        CNN_Model.model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(n_steps_in, n_features)))
        CNN_Model.model.add(MaxPooling1D(pool_size=2))
        CNN_Model.model.add(Flatten())
        CNN_Model.model.add(Dense(50, activation='relu'))
        CNN_Model.model.add(Dense(n_steps_out))
        CNN_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        CNN_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction
    def predict(self, pred, n_steps_in,n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1,n_steps_in,n_features))
        yhat = CNN_Model.model.predict(x_input, verbose=0)
        return yhat



class LSTM_Model(Pre_data,metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch
                            
    def build(self, n_steps_in,n_steps_out,n_features,X,y):
        n_features = X.shape[2]
                            
        LSTM_Model.model.add(
            LSTM(100, activation='relu', return_sequences=True, input_shape=(n_steps_in,n_features)))
        LSTM_Model.model.add(
            LSTM(100, activation='relu'))
        
        LSTM_Model.model.add(Dense(n_steps_out))
        LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps_in,n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps_in,n_features))
        yhat = LSTM_Model.model.predict(x_input, verbose=0)
        return yhat





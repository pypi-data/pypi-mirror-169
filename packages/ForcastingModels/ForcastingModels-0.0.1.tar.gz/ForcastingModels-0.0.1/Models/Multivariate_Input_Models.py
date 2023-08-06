from numpy import array, hstack
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, LSTM, Input, concatenate
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

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
    
class MLP_Model(Pre_data,metaclass=Singleton):
    model = Sequential()
    n_input = None

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, X, y):
        MLP_Model.n_input = X.shape[1] * X.shape[2]
        X = X.reshape((X.shape[0], MLP_Model.n_input))
        MLP_Model.model.add(Dense(100, activation='relu',
                            input_dim=MLP_Model.n_input))
        MLP_Model.model.add(Dense(1))
        MLP_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred):
        x_input = array(pred)
        x_input = x_input.reshape((1, MLP_Model.n_input))
        yhat = MLP_Model.model.predict(x_input, verbose=0)
        return yhat



class MLP_Headed_Model(Pre_data,metaclass=Singleton):
    model = None
    def __init__(self, epoch):
        self.epochs = epoch



    def build(self, n_steps, X, y):
        X1 = X[:, :, 0]
        X2 = X[:, :, 1]
        # first input model
        visible1 = Input(shape=(n_steps,))
        dense1 = Dense(100, activation='relu')(visible1)
        # second input model
        visible2 = Input(shape=(n_steps,))
        dense2 = Dense(100, activation='relu')(visible2)
        # merge input models
        merge = concatenate([dense1, dense2])
        output = Dense(1)(merge)
        MLP_Headed_Model.model = Model(
            inputs=[visible1, visible2], outputs=output)
        MLP_Headed_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Headed_Model.model.fit([X1, X2], y, epochs=self.epochs, verbose=0)

    def predict(self, pred, n_steps):
        x_input = array(pred)
        x1 = x_input[:, 0].reshape((1, n_steps))
        x2 = x_input[:, 1].reshape((1, n_steps))
        yhat = MLP_Headed_Model.model.predict([x1, x2], verbose=0)
        return yhat



class CNN_Model(Pre_data,metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features, X, y):
        CNN_Model.model.add(Conv1D(filters=64, kernel_size=2,
                            activation='relu', input_shape=(n_steps, n_features)))
        CNN_Model.model.add(MaxPooling1D(pool_size=2))
        CNN_Model.model.add(Flatten())
        CNN_Model.model.add(Dense(50, activation='relu'))
        CNN_Model.model.add(Dense(1))
        CNN_Model.model.compile(optimizer='adam', loss='mse')
    # fit model
        CNN_Model.model.fit(X, y, epochs=self.epochs, verbose=0)

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = CNN_Model.model.predict(x_input, verbose=0)
        return yhat



class CNN_Headed_Model(Pre_data,metaclass=Singleton):
    model = None

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features, X, y):
        # separate input data
        X1 = X[:, :, 0].reshape(X.shape[0], X.shape[1], n_features)
        X2 = X[:, :, 1].reshape(X.shape[0], X.shape[1], n_features)
        # first input model
        visible1 = Input(shape=(n_steps, n_features))
        cnn1 = Conv1D(filters=64, kernel_size=2, activation='relu')(visible1)
        cnn1 = MaxPooling1D(pool_size=2)(cnn1)
        cnn1 = Flatten()(cnn1)
        # second input model
        visible2 = Input(shape=(n_steps, n_features))
        cnn2 = Conv1D(filters=64, kernel_size=2, activation='relu')(visible2)
        cnn2 = MaxPooling1D(pool_size=2)(cnn2)
        cnn2 = Flatten()(cnn2)
        # merge input models
        merge = concatenate([cnn1, cnn2])
        dense = Dense(50, activation='relu')(merge)
        output = Dense(1)(dense)
        CNN_Headed_Model.model = Model(
            inputs=[visible1, visible2], outputs=output)
        CNN_Headed_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        CNN_Headed_Model.model.fit([X1, X2], y, epochs=self.epochs, verbose=0)

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x1 = x_input[:, 0].reshape((1, n_steps, n_features))
        x2 = x_input[:, 1].reshape((1, n_steps, n_features))
        yhat = CNN_Headed_Model.model.predict([x1, x2], verbose=0)
        return yhat



class LSTM_Model(Pre_data,metaclass=Singleton):
    model = Sequential()
    n_input = None

    def __init__(self, epoch):
        self.epochs = epoch


    def build(self, n_steps, n_features, X, y):
        LSTM_Model.model.add(
            LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
        LSTM_Model.model.add(Dense(1))
        LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = LSTM_Model.model.predict(x_input, verbose=0)
        return yhat


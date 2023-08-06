from numpy import array, hstack
from keras.models import Sequential,Model
from keras.layers import Dense, Flatten, LSTM,Input
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
        n_output = y.shape[1]
        MLP_Model.model.add(Dense(100, activation='relu',
                            input_dim=MLP_Model.n_input))
        MLP_Model.model.add(Dense(n_output))
        MLP_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred):
        x_input = array(pred)
        x_input = x_input.reshape((1, MLP_Model.n_input))
        yhat = MLP_Model.model.predict(x_input, verbose=0)
        return yhat


class MLP_Mul_out_Model(Pre_data,metaclass=Singleton):
    model = None
    n_input = None

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, X, y):
        MLP_Mul_out_Model.n_input = X.shape[1] * X.shape[2]
        X = X.reshape((X.shape[0], MLP_Mul_out_Model.n_input))
        # separate output
        y1 = y[:, 0].reshape((y.shape[0], 1))
        y2 = y[:, 1].reshape((y.shape[0], 1))
        y3 = y[:, 2].reshape((y.shape[0], 1))
        # define model
        visible = Input(shape=(MLP_Mul_out_Model.n_input,))
        dense = Dense(100, activation='relu')(visible)
        # define output 1
        output1 = Dense(1)(dense)
        # define output 2
        output2 = Dense(1)(dense)
        # define output 2
        output3 = Dense(1)(dense)
        # tie together
        MLP_Mul_out_Model.model = Model(inputs=visible, outputs=[output1, output2, output3])
        MLP_Mul_out_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Mul_out_Model.model.fit(X, [y1,y2,y3], epochs=self.epochs, verbose=0)
    def predict(self, pred, n_steps):
        x_input = array(pred)
        x_input = x_input.reshape((1, MLP_Mul_out_Model.n_input))
        yhat = MLP_Mul_out_Model.model.predict(x_input, verbose=0)
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
        CNN_Model.model.add(Dense(n_features))
        CNN_Model.model.compile(optimizer='adam', loss='mse')
    # fit model
        CNN_Model.model.fit(X, y, epochs=self.epochs, verbose=0)

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = CNN_Model.model.predict(x_input, verbose=0)
        return yhat

        
class CNN_Mul_out_Model(Pre_data,metaclass=Singleton):
    model = None
    n_input = None

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps,n_features,X, y):
        y1 = y[:, 0].reshape((y.shape[0], 1))
        y2 = y[:, 1].reshape((y.shape[0], 1))
        y3 = y[:, 2].reshape((y.shape[0], 1))
        # define model
        visible = Input(shape=(n_steps, n_features))
        cnn = Conv1D(filters=64, kernel_size=2, activation='relu')(visible)
        cnn = MaxPooling1D(pool_size=2)(cnn)
        cnn = Flatten()(cnn)
        cnn = Dense(50, activation='relu')(cnn)
        # define output 1
        output1 = Dense(1)(cnn)
        # define output 2
        output2 = Dense(1)(cnn)
        # define output 3
        output3 = Dense(1)(cnn)
        # tie together
        CNN_Mul_out_Model.model = Model(inputs=visible, outputs=[output1, output2, output3])
        CNN_Mul_out_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        CNN_Mul_out_Model.model.fit(X, [y1,y2,y3], epochs=2000, verbose=0)
    def predict(self, pred, n_steps,n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = CNN_Mul_out_Model.model.predict(x_input, verbose=0)
        return yhat


class LSTM_Model(Pre_data,metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features,X,y):
        LSTM_Model.model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
        LSTM_Model.model.add(Dense(1))
        LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        LSTM_Model.model.fit(X, y, epochs=200, verbose=0)

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = LSTM_Model.model.predict(x_input, verbose=0)
        return yhat





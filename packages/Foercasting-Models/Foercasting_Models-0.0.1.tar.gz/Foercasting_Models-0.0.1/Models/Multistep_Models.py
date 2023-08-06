from numpy import array
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, TimeDistributed, RepeatVector
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MLP_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    # using for univariate multistep

    def build(self, n_steps_in, n_steps_out, X, y):
        MLP_Model.model.add(Dense(100, activation='relu', input_dim=n_steps_in))
        MLP_Model.model.add(Dense(n_steps_out))
        MLP_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps_in):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps_in))
        yhat = MLP_Model.model.predict(x_input, verbose=0)
        return yhat


class CNN_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps_in, n_features, n_steps_out, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        CNN_Model.model.add(Conv1D(filters=64, kernel_size=2,
                                   activation='relu', input_shape=(n_steps_in, n_features)))
        CNN_Model.model.add(MaxPooling1D(pool_size=2))
        CNN_Model.model.add(Flatten())
        CNN_Model.model.add(Dense(50, activation='relu'))
        CNN_Model.model.add(Dense(n_steps_out))
        CNN_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        CNN_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps_in, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps_in, n_features))
        yhat = CNN_Model.model.predict(x_input, verbose=0)
        return yhat


class Vector_output_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps_in, n_features, n_steps_out, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))

        Vector_output_Model.model.add(
            LSTM(100, activation='relu', input_shape=(n_steps_in, n_features)))
        Vector_output_Model.model.add(
            LSTM(100, activation='relu'))
        Vector_output_Model.model.add(Dense(n_steps_out))
        Vector_output_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        Vector_output_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps_in, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps_in, n_features))
        yhat = Vector_output_Model.model.predict(x_input, verbose=0)
        return yhat


class Encoder_decoder_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps_in, n_features, n_steps_out, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        y = y.reshape((X.shape[0], X.shape[1], n_features))

        Encoder_decoder_Model.model.add(LSTM(
            100, activation='relu', input_shape=(n_steps_in, n_features)))
        Encoder_decoder_Model.model.add(RepeatVector(n_steps_out))
        Encoder_decoder_Model.model.add(LSTM(100, activation='relu', return_sequences=True))
        Encoder_decoder_Model.model.add(TimeDistributed(Dense(1)))
        Encoder_decoder_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        Encoder_decoder_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps_in, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps_in, n_features))
        yhat = Encoder_decoder_Model.model.predict(x_input, verbose=0)
        return yhat

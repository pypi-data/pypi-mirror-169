from numpy import array
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, Bidirectional, TimeDistributed, ConvLSTM2D
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

    # using for univariate

    def build(self, n_steps, X, y):
        MLP_Model.model.add(Dense(100, activation='relu', input_dim=n_steps))
        MLP_Model.model.add(Dense(1))
        MLP_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        MLP_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps))
        yhat = MLP_Model.model.predict(x_input, verbose=0)
        return yhat


class CNN_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        CNN_Model.model.add(Conv1D(filters=64, kernel_size=2,
                                   activation='relu', input_shape=(n_steps, n_features)))
        CNN_Model.model.add(MaxPooling1D(pool_size=2))
        CNN_Model.model.add(Flatten())
        CNN_Model.model.add(Dense(50, activation='relu'))
        CNN_Model.model.add(Dense(1))
        CNN_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        CNN_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = CNN_Model.model.predict(x_input, verbose=0)
        return yhat


class Vanilla_LSTM_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        Vanilla_LSTM_Model.model.add(
            LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
        Vanilla_LSTM_Model.model.add(Dense(1))
        Vanilla_LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        Vanilla_LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = Vanilla_LSTM_Model.model.predict(x_input, verbose=0)
        return yhat


class Stacked_LSTM_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        Stacked_LSTM_Model.model.add(LSTM(
            50, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
        Stacked_LSTM_Model.model.add(LSTM(50, activation='relu'))
        Stacked_LSTM_Model.model.add(Dense(1))
        Stacked_LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        Stacked_LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = Stacked_LSTM_Model.model.predict(x_input, verbose=0)
        return yhat


class Bidirectional_LSTM_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_steps, n_features, X, y):
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        Bidirectional_LSTM_Model.model.add(Bidirectional(
            LSTM(50, activation='relu'), input_shape=(n_steps, n_features)))
        Bidirectional_LSTM_Model.model.add(Dense(1))
        Bidirectional_LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        Bidirectional_LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = Bidirectional_LSTM_Model.model.predict(x_input, verbose=0)
        return yhat


class CNN_LSTM_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_seq, n_steps, n_features, X, y):
        X = X.reshape((X.shape[0], n_seq, n_steps, n_features))
        CNN_LSTM_Model.model.add(TimeDistributed(Conv1D(
            filters=64, kernel_size=1, activation='relu'), input_shape=(None, n_steps, n_features)))
        CNN_LSTM_Model.model.add(TimeDistributed(MaxPooling1D(pool_size=2)))
        CNN_LSTM_Model.model.add(TimeDistributed(Flatten()))
        CNN_LSTM_Model.model.add(LSTM(50, activation='relu'))
        CNN_LSTM_Model.model.add(Dense(1))
        CNN_LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        CNN_LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)

    def predict(self, pred, n_seq, n_steps, n_features):
        # demonstrate prediction
        x_input = array(pred)
        x_input = x_input.reshape((1, n_seq, n_steps, n_features))
        yhat = CNN_LSTM_Model.model.predict(x_input, verbose=0)
        return yhat


class Conv_LSTM_Model(metaclass=Singleton):
    model = Sequential()

    def __init__(self, epoch):
        self.epochs = epoch

    def build(self, n_seq, n_steps, n_features, X, y):
        X = X.reshape((X.shape[0], n_seq, 1, n_steps, n_features))
        Conv_LSTM_Model.model.add(ConvLSTM2D(filters=64, kernel_size=(
            1, 2), activation='relu', input_shape=(n_seq, 1, n_steps, n_features)))
        Conv_LSTM_Model.model.add(Flatten())
        Conv_LSTM_Model.model.add(Dense(1))
        Conv_LSTM_Model.model.compile(optimizer='adam', loss='mse')
        # fit model
        Conv_LSTM_Model.model.fit(X, y, epochs=self.epochs, verbose=0)
        # demonstrate prediction

    def predict(self, pred, n_seq, n_steps, n_features):
        x_input = array(pred)
        x_input = x_input.reshape((1, n_seq, 1, n_steps, n_features))
        yhat = Conv_LSTM_Model.model.predict(x_input, verbose=0)
        return yhat

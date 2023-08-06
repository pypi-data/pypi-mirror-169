#!/usr/bin/env python
# coding: utf-8

# In[15]:


from Functions import *
 
# convert history into inputs and outputs
class Singleton(type):
    __instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]
class LSTM_Power(metaclass=Singleton): 
    # load the new file
    dataset = read_csv('F:\link3\household_power_consumption_days.csv', header=0, infer_datetime_format=True, parse_dates=['datetime'], index_col=['datetime'])
# split into train and test
    train, test =split_dataset(dataset.values)
# evaluate model and get scores
    n_input = 7
    score, scores = evaluate_model(train, test, n_input)
# summarize scores
    summarize_scores('lstm', score, scores)
# plot scores
    days = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    def to_supervised(self,train, n_input, n_out=7):
# flatten data
        data = train.reshape((train.shape[0]*train.shape[1], train.shape[2]))
        X, y = list(), list()
        in_start = 0
# step over the entire history one time step at a time
        for _ in range(len(data)):
# define the end of the input sequence
            in_end = in_start + n_input
            out_end = in_end + n_out
# ensure we have enough data for this instance
            if out_end <= len(data):
                x_input = data[in_start:in_end, 0]
                x_input = x_input.reshape((len(x_input), 1))
                X.append(x_input)
                y.append(data[in_end:out_end, 0])
# move along one time step
            in_start += 1
        return array(X), array(y)
 
# train the model
    def build_model(self,train, n_input):
# prepare data
        train_x, train_y =self.to_supervised(train, n_input)
# define parameters
        verbose, epochs, batch_size = 0, 70, 16
        n_timesteps, n_features, n_outputs = train_x.shape[1], train_x.shape[2], train_y.shape[1]
# define model
        model = Sequential()
        model.add(LSTM(200, activation='relu', input_shape=(n_timesteps, n_features)))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(n_outputs))
        model.compile(loss='mse', optimizer='adam')
# fit network
        model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=verbose)
        return model
 
# make a forecast
    def forecast(self,model, history, n_input):
    # flatten data
        data = array(history)
        data = data.reshape((data.shape[0]*data.shape[1], data.shape[2]))
    # retrieve last observations for input data
        input_x = data[-n_input:, 0]
   # reshape into [1, n_input, 1]
        input_x = input_x.reshape((1, len(input_x), 1))
# forecast the next week
        yhat = model.predict(input_x, verbose=0)
  # we only want the vector forecast
        yhat = yhat[0]
        return yhat
 
# evaluate a single model
    def evaluate_model(self,train, test, n_input):
# fit model
            model = self.build_model(train, n_input)
 # history is a list of weekly data
            history = [x for x in train]
# walk-forward validation over each week
            predictions = list()
            for i in range(len(test)):
 # predict the week
                 yhat_sequence = self.forecast(model, history, n_input)
# store the predictions
                 predictions.append(yhat_sequence)
# get real observation and add to history for predicting the next week
                 history.append(test[i, :])
# evaluate predictions days for each week
            predictions = array(predictions)
            score, scores = self.evaluate_forecasts(test[:, :, 0], predictions)
            return score, scores
 

    pyplot.plot(days, scores, marker='o', label='lstm')
    pyplot.show()


# In[ ]:





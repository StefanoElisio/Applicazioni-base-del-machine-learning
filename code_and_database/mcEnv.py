import csv
import random
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class machine_learner:
    def __init__(self,data_url,use_Case,n_da_stimare,random_seed):
        #varifica se c'è un seed e in caso lo applica
        if random_seed is not None:
            random.seed(random_seed)
            np.random.seed(random_seed)

        data = self.reader(data_url)
        self._piante_adatte = []

        #decide se il programma sarà un test o una predizione
        if use_Case == None:
            self.data_preparation(data,'test')
            model = self.RFC_trainer(self.X_train,self.y_train)
            self._prediction = model.predict(self.X_test)
        else:
            for i in range(n_da_stimare):
                self.data_preparation(data,'prediction')
                model = self.RFC_trainer(self._X,self._y)
                self._prediction = model.predict(use_Case)
                self._piante_adatte.append(self._prediction[0])

    def reader(self,data_url):
        '''legge il file in input e lo salva in un database(data)'''
        with open(data_url, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)
            data = []
            for row in reader:
                row = [value for value in row]
                data.append(row)
                data = random.sample(data, len(data))
        return data

    def data_preparation(self,data,type):
        '''usa i dati del database e lo divine in dati di input(X) e di output(y)'''
        self._X = []
        self._y = []
        for row in data:
            if row[7] not in self._piante_adatte:
                self._X.append([float(row[i]) for i in range(7)])
                self._y.append(row[7])

        #se il programma deve fare un test divide ulteriormente X e y in un train set e un test set
        if type == 'test':
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self._X,self._y,test_size=0.2,random_state=16)

    def RFC_trainer(self,X,y):
        '''allena il modello'''
        model = RandomForestClassifier()
        model.fit(X,y)
        return model

    def get_Prediction(self):
        return self._prediction
    def get_piante_adatte(self):
        return self._piante_adatte




class Ortaggi():
    def __init__(self):
        '''Crea una lista in cui associa ad ogni ortaggio del database una produzione Kg/m^2 e un prezzo al Kg'''
        self._list=[('rice' ,5 ,3 ),
                    ( 'maize' ,4 ,0.5 ),
                    ( 'chickpea' ,0.75 ,2.5 ),
                    ( 'kidneybeans' ,1.5 ,3.25 ),
                    ( 'pigeonpeas' ,1.5 ,2.75 ),
                    ( 'mothbeans' ,0.75 ,3.5 ),
                    ( 'mungbean' ,3 ,2 ),
                    ( 'blackgram' ,0.75 ,2 ),
                    ( 'lentil' ,1.5 ,3.25 ),
                    ( 'pomegranate' ,10 ,3.5 ),
                    ( 'banana' ,25 ,2 ),
                    ( 'mango' ,17.5 ,4 ),
                    ( 'grapes' ,20 ,3 ),
                    ( 'watermelon' ,10 ,1.25 ),
                    ( 'muskmelon' ,12.5 ,2 ),
                    ( 'apple' ,20 ,2 ),
                    ( 'orange' ,22.5 ,2 ),
                    ( 'papaya' ,22.5 ,3.5 ),
                    ( 'coconut' ,20 ,5 ),
                    ( 'cotton' ,3 ,2 ),
                    ( 'jute' ,2 ,2 ),
                    ( 'coffee' ,3.5 ,7.5 )]

    def getValue(self, x):
        '''Restistuisce il valore di un ortaggio
        ovvero il guadagno atteso per metro quadrato:
        produzione * prezzo'''
        for ort in self._list:
            if ort[0] == x: return ort[1] * ort[2]

    def getProd(self, x):
        for ort in self._list:
            if ort[0] == x: return ort[1]

    def getPrice(self, x):
        for ort in self._list:
            if ort[0] == x: return ort[2]





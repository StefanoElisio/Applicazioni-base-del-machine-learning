from mcEnv import machine_learner
from cspEnv import cspEnv
from ortaggi import Ortaggi
from pathlib import Path


_SEED = 16

#il comportamento del ML varia per ogni esecuzione
#_SEED = None

#in quest'ordine:N,P,K, temperature,humidity,   ph,         rainfall
_TEST_CASE = [[39,9,15,25.35467646,91.81183218,7.992041984,116.7555937]]

#effettua un controllo sull'accuratezza del machine learner
#_TEST_CASE = None

p=Path(__file__)
_DATABASE = p.parent.absolute() / 'Crop_recommendation.csv'

_FARMIMG_SPACE = 10000 #metri quadrati
_FARM_CAPACITY = 200000 #chili


'''inizio main'''
if __name__ == '__main__':

    '''creazione classe ortaggi'''
    ortaggi = Ortaggi()

    '''Risoluzione problema del machine learning'''
    mc = machine_learner(_DATABASE,_TEST_CASE,4,_SEED)

    if _TEST_CASE is not None:

        '''Risoluzione CSP'''
        csp = cspEnv(ortaggi,mc.get_piante_adatte(),_FARMIMG_SPACE,_FARM_CAPACITY)

        '''Stampa del risultato'''
        print('le piante più adatte al tuo terreno sono', mc.get_piante_adatte())
        if csp._prob.status == 1:
            tot_occ = 0
            tot_ven = 0
            tot_cap = 0
            for v in csp._prob.variables():
                print(v.name, '=', v.varValue, 'metri quadri')
                tot_occ += v.varValue
                tot_ven += v.varValue * ortaggi.getValue(v.name)
                tot_cap += v.varValue * ortaggi.getProd(v.name)
            print('terreno occupato =', tot_occ, 'su', _FARMIMG_SPACE, 'm^2')
            print('prezzo di vendita =', tot_ven, "$")
            print('storage usato =', tot_cap, 'su', _FARM_CAPACITY, 'Kg')
        else:
            print('non è stato possibile trovare una soluzione con i dati inseriti')

    else:
        print('***** TEST SUL SISTEMA DI MACHINE LEARNING ***** \n')
        prediction = mc.get_Prediction()
        test_set = mc.y_test
        errors = 0
        for i in range(len(test_set)):
            if prediction[i] != test_set[i]: errors += 1
        success_rate = (1-(errors / len(test_set))) * 100
        print('su', len(test_set), 'predizioni il programma ne ha sbagliate', errors)
        print('con un percentuale di successo del', success_rate, '%')



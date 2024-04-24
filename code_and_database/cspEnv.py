from pulp import LpVariable, LpProblem, LpMaximize

class cspEnv:
    def __init__(self,ortaggi, crops, farmimg_space, farm_storage):
        self._prob = LpProblem("Optimization_Problem", LpMaximize)
        var = self.build_Variables(crops)
        self.build_Constraints(var,crops,ortaggi,farmimg_space,farm_storage)
        self.solve()

    def build_Variables(self,crops):
        '''Costruisce 4 variabili continue positive, che rappresentano in ordine i 4 ortaggi'''
        w = LpVariable(str(crops[0]), lowBound=0, cat='Continuous')
        x = LpVariable(str(crops[1]), lowBound=0, cat='Continuous')
        y = LpVariable(str(crops[2]), lowBound=0, cat='Continuous')
        z = LpVariable(str(crops[3]), lowBound=0, cat='Continuous')
        return [w, x, y, z]

    def build_Constraints(self,var,crops,ortaggi,farmimg_space,farm_storage):
        '''Costruisce la funzione obiettivo e i vincoli del problema'''
        w,x,y,z = var
        #funzione obiettivo
        self._prob += ortaggi.getValue(str(crops[0])) * w + ortaggi.getValue(str(crops[1])) * x + ortaggi.getValue(str(crops[2])) * y + ortaggi.getValue(str(crops[3])) * z
        #vincoli
        self._prob += w + x + y + z <= farmimg_space
        self._prob += w + x + y + z >= farmimg_space*(3/4)
        self._prob += w >= farmimg_space / 20
        self._prob += x >= farmimg_space / 20
        self._prob += y >= farmimg_space / 20
        self._prob += z >= farmimg_space / 20
        self._prob += (ortaggi.getProd(str(crops[0])) * w + ortaggi.getProd(str(crops[1])) * x + ortaggi.getProd(str(crops[2])) * y + ortaggi.getProd(str(crops[3])) * z) <= farm_storage

    def solve(self):
        '''risolve il problema CSP'''
        print('***** INIZIO RISOLUZIONE DEL CSP ***** \n')
        self._prob.solve()
        print('***** FINE RISOLUZIONE PROBLEMA ***** \n')
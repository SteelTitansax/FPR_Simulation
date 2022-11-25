
#Design equation of an FPR
#-------------------------
#Libraries
#Variable declarations
#---------------------

from scipy.integrate import quad
k = 0.3 #1/min
Ca0= 10 #mol/l
V0 = 10 #l/min
Fa0 = Ca0 * V0
X = 0.8
#Kinetics
#--------
def rA(X):
    Ca = Ca0*(1-X)
    return -k*Ca

def integral(X):
    return Fa0/-rA(X)

V,err = quad(integral,0,X)
print("Volumen : " + str(V) )




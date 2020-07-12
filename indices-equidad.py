import numpy as np
import re
import pandas as pd
import math
import statistics
from matplotlib import pyplot as plt


#from matplotlib import pyplot as plt
#import quantecon as qe
#from numba import njit, jitclass, float64, prange
    
def main():
    arrayTResp=np.array([23152.40426, 23352.67391, 23226.56522, 23281.173913, 23382.260870,
                23633.244444, 23528.422222, 23258.913043, 23217.086957, 23223.782609,
                23379.760870, 23358.586957, 23383.130435, 23426.739130, 23286.304348,
                23267.804348, 23214.891304, 23037.319149, 23393.239130, 23406.913043,
                23449.217391, 23159.043478, 23300.152174, 23555.111111, 23394.913043, 
                23299.108696, 23323.913043, 23423.304348, 23667.866667, 23285.000000])
    # Media (m)
    m = np.mean(arrayTResp)
    # Desviacion estandas (s)
    s =  statistics.stdev(arrayTResp)
    # Coeficiente de variacion (CoV)
    CoV = s/m
    # Para calcular la senial para el ratio de ruido
    n = len(arrayTResp)
    finalIntervalo = math.sqrt(n-1)

    # Desviacion de la media absoluta (MAD) 
    series = pd.Series(arrayTResp) 
    mad = series.mad() 

    # Indice de equidad de Gini (iegini)
    iegini = gini(arrayTResp)

    # Gap de lorenz (gap)
    gap= mad/(2*m)
    
    lorentz_curve(arrayTResp)

    # Indice de equidad de Jain
    jie = jain(arrayTResp)
   
    # Imprimir por pantalla los resultados obtenidos
    print(""" Media: %f """% (m))
    print(""" Derivacion estandar: %f """% (s))
    print(""" Coeficiente de derivacion: %f """% (CoV))
    print(""" Signal to noise ratio: 0 <= %f <= %f """% (CoV, finalIntervalo))
    print(""" Mean Absolute Deviation: %f """% (mad))
    print(""" 0 <= MAD <= s --> 0<= %f <= %f """% (mad,s))
    print(""" Gap de Lorenz: %f """% (gap))
    print(""" Indice de equidad de Jain %f """% (jie))
    print(""" Indice de equidad de Gini %f """% (iegini))
def jain(arr):
    denominador = 0
    numerador =  sum(arr)**2
    for dato in arr:
        denominador = denominador + dato**2

    denominador = denominador*len(arr)
    jie = numerador/denominador
    return jie

def gini(arr):
    ## first sort
    sorted_arr = arr.copy()
    sorted_arr.sort()
    n = arr.size
    coef_ = 2. / n
    const_ = (n + 1.) / n
    weighted_sum = sum([(i+1)*yi for i, yi in enumerate(sorted_arr)])
    return coef_*weighted_sum/(sorted_arr.sum()) - const_

def dist_lorentz(x):
    import numpy as np
    
    y = np.array(x)           # y-axis data
    y = np.sort(y, kind='mergesort')

    x = np.repeat(1, len(y))  # x-axis data

    pct_x = x / sum(x)        # x normalized
    pct_x = np.cumsum(pct_x)  # CDF x

    pct_y = y / sum(y)        # y normalized
    pct_y = np.cumsum(pct_y)  # CDF y

    # starts with (0,0)

    pct_y = np.insert(pct_y, 0, 0) 
    pct_x = np.insert(pct_x, 0, 0)

    return pct_x, pct_y

def lorentz_curve(x):
    
    import matplotlib.pyplot as plt
    
    # weight case
    
    x, y = dist_lorentz(x)
    
    fig = plt.figure(figsize=(5,5))

    plt.plot(x, y, 'r-', alpha=0.7) # curva de lorentz
    plt.plot([0,1],[0,1], color='black') # line 45º

   # plt.xlabel('CDF x (%)')
   # plt.ylabel('CDF y (%)')

    plt.suptitle('Curva de Lorenz', fontsize=15)
    plt.xlim(0,1)
    plt.ylim(0,1)
    return plt.show()

if __name__ == "__main__":
    main()
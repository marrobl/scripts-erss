import numpy as np
import re
import pandas as pd
import math
import statistics
from matplotlib import pyplot as plt


def main():
    datos = pd.read_csv('./datosEjercicio1_local-recortado.csv')
  
    datos2 = datos[datos['threadName'].str.contains(' AlumnosRdto 1-30')]
    # df['col1'].str.contains('^') 
    arrayTResp  = datos2['elapsed'].values
  
    
    # Media (m)
    m = arrayTResp.mean()
    print("""Media %f"""%(m))
if __name__ == "__main__":
    main()
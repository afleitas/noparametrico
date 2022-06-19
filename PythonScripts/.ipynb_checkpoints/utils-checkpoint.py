import pandas as pd
import numpy as np
from scipy.stats import binom


def binomial_interval(alfa,ps,r,n):
    liminf = []
    limsup = []
    for x in range(1,len(ps)):
        liminf.append(binom.cdf(r-1, n, ps[x-1]))
        limsup.append(binom.cdf(r, n, ps[x-1]))    
    minp=[]
    maxp=[]
    for p in range(2,len(ps)):
        if liminf[p-1]<=(1-alfa) and liminf[p-2]>(1-alfa):
            minp.append(ps[p-2])
        if limsup[p-1]<=(alfa) and limsup[p-2]>(alfa):
            maxp.append(ps[p-2])
    return  {'Li':minp[0],'Ls':maxp[0]} 




def test_binomial(r,n,p0,alfa,tipo:str):

    if tipo=="izquierda":
        
        nivel_significacion=[]
        k=[]
        
        for x in range(0,n+1):
            if binom.cdf(x, n, p0)<= alfa:
                nivel_significacion.append(binom.cdf(x, n, p0))
                k.append(x)
        
        nivel_significacion = np.max(nivel_significacion)
        k = np.max(k)+1
        pvalor = binom.cdf(r, n, p0)        
        output = {'nivel_significacion': nivel_significacion, 'k': k,'p_estimado':r/n ,'pvalor':pvalor}
        
    

    if tipo=="derecha":
        
        nivel_significacion=[]
        k=[]
        
        for x in range(0,n+1):
            if binom.cdf(x, n, p0)>alfa:
                nivel_significacion.append(binom.cdf(x, n, p0))
                k.append(x)
                
        nivel_significacion = np.min(nivel_significacion)
        k = np.min(k)
        pvalor = 1-binom.cdf(r-1, n, p0)        
        output = {'nivel_significacion': nivel_significacion, 'k': k,'p_estimado':r/n, 'pvalor':pvalor}
        

    if tipo=="bilateral":
        
        nivel_significacion=[]
        k=[]
        
        for x in range(0,n+1):
            if binom.cdf(x, n, p0)<= alfa/2:
                nivel_significacion.append(binom.cdf(x, n, p0))
                k.append(x)
        
        nivel_significacion = np.max(nivel_significacion)
        k = np.max(k)+1
        pvalor = binom.cdf(r, n, p0)*2        
        output = {'nivel_significacion': nivel_significacion, 'k': k,'p_estimado':r/n ,'pvalor':pvalor}
        
                
    return output
       
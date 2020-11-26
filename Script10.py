# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:40:36 2020

@author: Luis Navarro
"""
# =============================================================================
# Scripts tarea 10
# =============================================================================
import math 
import sys 
import numpy as np 

# Raices cúbicas
def cubroots(P,Q,R,FASE):    
    # A1 = P ; A2 = Q ; A3 = R
    import sys 

    ALFA=(3.0*Q-P*P)/3.0
    BETA=(2.0*P*P*P-9.0*P*Q+27.0*R)/27.0
    DELTA=(BETA*BETA)/4.0+(ALFA*ALFA*ALFA)/27.0
    
    if(DELTA<0.0): 
        COSPHI=-BETA/(2.0*math.sqrt(-ALFA*ALFA*ALFA/27.0))
        PHI=math.acos(COSPHI)
        X1=2.0*math.sqrt(-ALFA/3.0)*math.cos(PHI/3.0)-P/3.0
        X2=2.0*math.sqrt(-ALFA/3.0)*math.cos(PHI/3.0+2.0*3.1416/3.0)-P/3.0
        X3=2.0*math.sqrt(-ALFA/3.0)*math.cos(PHI/3.0+4.0*3.14160/3.0)-P/3.0
        #NROOT=3    !hugo
        # fase liquida:menor Z ; fase gas:maior Z
        if FASE=="L":
            X=X1
            if(X>X2): 
                X=X2
            if(X>X3): 
                X=X3
            if((X1<0.0)and(X2<0.0)and(X3<0.0)): 
                sys.exit('Tres raices Z son negativas fase:L')
            sys.exit('goto 1')       
        else:
            X=X1
            if(X<X2): 
                X=X2
            if(X<X3): 
                X=X3
            if((X1<0.0)and(X2<0.0)and(X3<0.0)):
                sys.exit('Tres raices Z son negativas, fase:V')         
            sys.exit('goto 1')            
              
    SQDEL=math.sqrt(DELTA)
    ACUB=-BETA/2.0+SQDEL
    ASIGN=ACUB/abs(ACUB)
    ACUB=abs(ACUB)
    A=ACUB**(1.0/3.0)
    A=ASIGN*A
    BCUB=-BETA/2.0-SQDEL
    BSIGN=BCUB/abs(BCUB)
    BCUB=abs(BCUB)
    B=BCUB**(1.0/3.0)
    B=BSIGN*B
    X=A+B-P/3.0
    #print('Fase :', FASE)
    #print('Z=', round(X,4))
    if(X<0.0): 
        sys.exit('Tres raices Z son negativas, fase:V')
    #print(X)
    return(X)

#Peng-Robinson
def PR(P,T,Tc,pc,w,FRMOL,kij,Fase):
    
    R = 10.73 #146
    ncomps = len(w)
    #print(ncomps)
    OmegaA = 0.45724
    OmegaB = 0.07780
    
    a=[]
    aa=[]
    
    b=[]
    #w=[]
    m=[]
    alpha=[]

    
    for L in range(ncomps):
        # a[L]=OmegaA*R*R*Tc[L]*Tc[L]/pc[L]
        a.append(OmegaA*R*R*Tc[L]*Tc[L]/pc[L])
        # b[L]=OmegaB*R*Tc[L]/pc[L]
        b.append(OmegaB*R*Tc[L]/pc[L])
        
    for L in range(ncomps):  
        
        if (w[L] <= 0.49):
            #m[L] = 0.37464+1.54226*w[L]-0.26992*w[L]**2
            m.append(0.37464+1.54226*w[L]-0.26992*w[L]**2)
            
        else:
            #m = 0.3796+1.485*w[L]-0.1644*w[L]**2+0.01667*w[L]**3
            m.append(0.3796+1.485*w[L]-0.1644*w[L]**2+0.01667*w[L]**3)

        #alpha[L]=(1+m[L]*(1-math.sqrt(T/Tc[L]))**2
        alpha.append((1+m[L]*(1-math.sqrt(T/Tc[L])))**2)
        #aa[L]=aa[L]*alpha[L]*alpha[L]
        aa.append(a[L]*alpha[L])
    
   
    #print('m', m)
    #print('alpha', alpha)
    #print('a_i', a)
    #print('b_i', b)
    
    A = 0
    B = 0
    
    for i in range(ncomps):
        B=B+FRMOL[i]*b[i]
        for j in range(ncomps):
            #aij[i][j]=math.sqrt(aa[i]*aa[j])*(1.0-kij[i][j])
            aij=math.sqrt(aa[i]*aa[j])*(1.0-kij[i][j])
            #A=A+aij[i][j]*FRMOL[i]*FRMOL[j]
            A=A+aij*FRMOL[i]*FRMOL[j]

    # print("aij:",aij)
    # print("A :",A)
    # print('Fase :', Fase)        
    # print('a*alpha_m =',A)
    # print('b_m =',B)

    AA=A*P/(R*R*T*T)  #Ec. 3.15 Firoozabadi    
    BB=B*P/(R*T)      #Ec. 3.16 Firoozabadi      
    
    #print(AA)
    #print (BB)
    A1=-(1.0-BB)
    A2= AA-3.0*BB*BB-2.0*BB
    A3=-(AA*BB-BB*BB-BB*BB*BB)
      
    #print(A1)
    #print(A2)
    #print(A3)
    # Calculate liquid and vapor phase roots
    Z = cubroots(A1, A2, A3, Fase)      
    
 
    return (Z)

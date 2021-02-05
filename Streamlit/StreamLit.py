import streamlit as st
import numpy as np 
#import matplotlib.pyplot as plt

st.title("Simulador de Gas")
st.write("""
## Variables de entrada
""")

st.sidebar("Variables de entrada")
Imax = st.sidebar.slider("Imax",0,100)
Re = 3280.08     #ft
Rw = 0.401      #ft
dz = 23         #ft 
Dt = 1          #sec
Perm = 1        #mD        
Vis = 0.0216  


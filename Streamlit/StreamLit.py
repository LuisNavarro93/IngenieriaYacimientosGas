import streamlit as st
import numpy as np 
#import matplotlib.pyplot as plt

st.title("Simulador de Gas")
st.write("""
## Variables de entrada
""")

Imax = st.sidebar.slider("Imax",0,100)
Re = st.sidebar.slider("Re",0,100)
Re = st.sidebar.slider("Re",0,1000)
Rw = st.sidebar.slider("Re",0,1000)
dz = st.sidebar.slider("Re",0,1000)
Dt = st.sidebar.slider("Re",0,1000)
Perm = st.sidebar.slider("Re",0,1000)
Vis = st.sidebar.slider("Re",0,1000)


import streamlit as st
import ipywidgets as wts
from IPython.display import display


st.title("Simulador de Gas")
st.write("""
## Variables de entrada
""")
Re = wts.FloatSlider(min=10,max=500,step=5,description='Re[ft]:',value=328.08) ; display(Re) ; 
Rw = wts.FloatSlider(min=0,max=5,step=.05,description='Rw[ft]:',value=0.401) ; display(Rw) 
dz = wts.FloatSlider(min=10,max=100,step=.05,description='dz[ft]:',value=23) ; display(dz) 
Perm = wts.FloatSlider(min=0,max=100,step=.05,description='k[mD]:',value=1) ; display(Perm) 
Vis = wts.FloatSlider(min=0,max=.1,step=.0015,description='mu[cP]:',value=0.0216) ; display(Vis) 
Cg = wts.FloatSlider(min=0,max=.1,step=.0001,description='Cg[1/psi]:',value=1.5e-4) ; display(Cg) 
Cf = wts.FloatSlider(min=0,max=.1,step=.0001,description='Cf[1/psi]:',value=3.5e-6) ; display(Cf)
Phi = wts.FloatSlider(min=0,max=1,step=0.1,description= 'Φ[frac]:',value=.18) ; display(Phi)
FVFg = wts.FloatSlider(min=0,max=1,step=.0001,description='Bg[ft/scf]:',value=0.02) ; display(FVFg) 
StoC = wts.FloatSlider(min=0,max=1,step=.0001,description='StoC:',value=0.01) ; display(StoC) 
Skin = wts.FloatSlider(min=-10,max=10,step=1,description='S:',value=5) ; display(Skin) ; Skin = Skin.value
Rate = wts.FloatSlider(min=-100000,max=10000,step=100,description='Gasto[scf/d]:',value=-1e6) ; display(Rate) 
PrsIni = wts.FloatSlider(min=0,max=10000,step=10,description='PrsIni[psi]:',value=6009) ; display(PrsIni) 
Imax = wts.IntSlider(min=10,max=100,step=5,description='Imax:',value=100) ; display(Imax) 
Tsim = wts.FloatSlider(min=1,max=100,step=1,description='Tsim[dias]:',value=10) ; display(Tsim) 
Dt = wts.FloatSlider(min=1,max=100,step=1,description='Δt[sec]:',value=1) ; display(Dt) 
Tshutin = wts.FloatSlider(min=1,max=1000,step=10,description='Tshut[dias]:',value=10) ; display(Tshutin) 

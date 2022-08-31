import pandas as pd
import numpy as np
import streamlit as st
import codecs 

st.title ("Cicle Rides in NYC")

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)

    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text(["Cargando datos..."])
data=load_data(501)
data_load_state.text("Los datos se cargaron")
agree=st.sidebar.checkbox("Show raw data")
if agree: 
  st.header("Raw data")
  st.dataframe(data)

data=load_data(500)

sidebar = st.sidebar
sidebar.title("Filtros:")


agree = st.sidebar.checkbox("Mostrar todos los registros")
if agree:
  st.dataframe(data)



agree2 = st.sidebar.checkbox("Mostrar todos los recorridos por hora")
if agree2:
  st.header("Numero recorridos por hora")
  hist_values=np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
  st.bar_chart(hist_values)


agree3=st.sidebar.slider("hour", 0,23,17)
if agree3: 
  filter_data=data[data[DATE_COLUMN].dt.hour==agree3]
  st.subheader("mapa recorridos iniciados a las %s:00" % agree3)
  st.map(filter_data)



    









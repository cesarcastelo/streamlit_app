import streamlit as st
import pandas as pd
import numpy as np
from datetime import time, datetime, date

# agregamos algunos elementos de texto
st.title('Titulo nuevo 2')
st.write('# Hola **como** estas')
st.write('### Hola **como** estas')

# agregamos un slider
num = st.slider("Numero 1", 0, 100, step=1)
st.write(f'Numero escogido: {num}')

# mostramos codigo
st.code("""
	import streamlit as st
import pandas as pd
import numpy as np

st.title('Titulo nuevo 2')
st.write('# Hola **como** estas')
st.write('## Hola **como** estas')
st.write('### Hola **como** estas')
num = st.slider("Numero 1", 0, 100, step=1)
st.code('Hola como estas')

st.write(f'Numero escogido: {num}')
""")

# creamos una formula matematica usando el lenguaje Latex
st.latex('\\sqrt{\\frac{x^2}{y^2+1+4xy}}')

# creamos un slider doble de tipo time
hora_evento = st.slider(
     "Programe la asesoria:",
     value=(time(11, 30), time(13, 30)))
st.write("Esta agendado desde {} hasta {}".format(hora_evento[0], hora_evento[1]))

# creamos un slider doble de tipo datetime
fecha_evento = st.slider(
     "Programe la asesoria:",
     min_value=datetime(2022, 11, 1),
     max_value=datetime(2022, 11, 30),
     value=(datetime(2022, 11, 1, 11, 30), datetime(2022, 11, 8, 13, 30)),
     format="DD/MM/YYYY - hh:mm")
st.write("Esta agendado desde {} hasta {}".format(fecha_evento[0], fecha_evento[1]))
st.write("El evento tiene una duracion de {}".format(fecha_evento[1]-fecha_evento[0]))

# creamos un calendario para ingreso de datos
d = st.date_input(
     "Fecha de cumpleaños",
     date(2019, 7, 6))
st.write('Tu cumpleaños es:', d)

# creamos una casilla de seleccion
option = st.selectbox(
     '¿Cómo desearía ser contactado/a?',
     ('Email', 'Teléfono', 'Whatsapp'),
     index=1)

st.write('Seleccionó:', option)

# creamos un plot de lineas a partir de un dataframe con datos aleatorios
n = st.slider("n", 5,1000, step=1)
chart_data = pd.DataFrame(np.array([np.random.randn(n), np.random.randn(n)]).T, columns=['data1', 'data2'])
st.line_chart(chart_data)

# creamos un dataframe com coordenadas y lo mostramos como un mapa
# df = pd.DataFrame(
#      np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#      columns=['lat', 'lon'])
df = pd.DataFrame(
	[[-12.043542584593608, -77.03599151024925]],
     columns=['lat', 'lon'])
st.map(df)

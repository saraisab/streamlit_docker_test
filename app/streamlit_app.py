import streamlit as st
from programa import ejecutar_suma

# sidebar
def pagina_principa():
    st.title("Pagina principal")
    st.write("bienvenido a la app de pruebas")

def ejemplo_2_func():
    st.title("Esta es la seguna pagina")
    st.write("esta es la pagina de ejemplo 2")

def ejemplo_label():
    title = st.text_input("Movie title", "Life of Brian")
    num_1 = st.number_input("Numero 1")
    num_2 = st.number_input("Numero 2")
    st.write(f'El resultado es: {ejecutar_suma(num_1, num_2)}')


st.sidebar.title("Navegación")

pagina = st.sidebar.selectbox('Selecciona una página', ['Pág. ppal', 'Visualización de datos', 'Gráficos interactivos'])

inicio = st.sidebar.button('programa 1')
ejemplo_2 = st.sidebar.button('programa 2')
ejemplo_3_bt = st.sidebar.button('labels')

if inicio:
    pagina_principa()
elif ejemplo_2:
    ejemplo_2_func()
elif ejemplo_3_bt:
    ejemplo_label()

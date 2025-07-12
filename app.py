import streamlit as st
import pandas as pd
import plotly.express as px

# Página principal
def pagina_principal():
    st.title("Página Principal")
    st.write("Bienvenido a la aplicación de demostración.")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")

# Página para visualizar datos
def visualizacion_datos():
    st.title("Visualización de Datos")
    st.write("Carga un archivo CSV para visualizar sus datos.")
    
    archivo_cargado = st.file_uploader("Sube un archivo CSV", type=["csv"])

    if archivo_cargado is not None:
        try:
            df = pd.read_csv(archivo_cargado)
            st.success("Archivo cargado correctamente ✅")
            st.write("Vista previa del archivo:")
            st.dataframe(df)
            st.write("Estadísticas descriptivas:")
            st.write(df.describe())
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")

# Página para gráficos interactivos
def graficos_interactivos():
    st.title("Gráficos Interactivos")
    st.write("Carga un archivo CSV para crear gráficos interactivos.")
    
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type=["csv"], key="2")

    if archivo_cargado is not None:
        try:
            df = pd.read_csv(archivo_cargado)
            st.write("Vista previa del archivo:")
            st.dataframe(df)

            eje_x = st.selectbox("Elige una columna para el eje X:", df.columns)
            eje_y = st.selectbox("Elige una columna para el eje Y:", df.columns)

            if st.button("Crear Gráfico"):
                fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
                st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")

# Configuración del menú lateral
st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página:", 
                              ["Página Principal", "Visualización de Datos", "Gráficos Interactivos"])

# Mostrar la página seleccionada
if pagina == "Página Principal":
    pagina_principal()
elif pagina == "Visualización de Datos":
    visualizacion_datos()
elif pagina == "Gráficos Interactivos":
    graficos_interactivos()


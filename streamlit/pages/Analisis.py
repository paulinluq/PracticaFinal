import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title='Starbucks Analysis', layout='wide',     page_icon="☕")

# Cargar datos
#@st.cache_data
#def load_data():
    #data = pd.read_csv('starbucks.csv')
    #return data

#df = load_data()
#df.columns = df.columns.str.strip()

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    mijson = r.json()
    listado = mijson['contratos']
    df = pd.DataFrame.from_records(listado)
    return df

df = load_data('http://fastapi:8000/retrieve_data')
df.columns = df.columns.str.strip()

# Ver las columnas de tu DataFrame como una tabla
#st.write("Columnas de la Base de Datos:")
#st.write(df.columns)

# Título del Dashboard
st.title('Dashboard de Análisis de Bebidas Starbucks')

# Filtros para el usuario
category = st.sidebar.multiselect('Selecciona la Categoría', options=df['Beverage_category'].unique(), default=df['Beverage_category'].unique())
beverages = df[df['Beverage_category'].isin(category)]


# Gráfico de Calorías por Bebida
st.header('Calorías por Bebida')
#fig = px.bar(beverages, x='Beverage', y='Calories', color='Beverage_category')
# Calcular la media de calorías por bebida
calories_mean_per_beverage = beverages.groupby('Beverage_category')['Calories'].mean().reset_index()

# Crear un gráfico de barras usando la media de calorías
fig = px.bar(calories_mean_per_beverage, x='Beverage_category', y='Calories', color='Beverage_category', color_discrete_sequence=px.colors.sequential.Greens,
             title='Media de Calorías por tipo de Bebida')

st.plotly_chart(fig, use_container_width=True)


# Gráfico de Contenido Nutricional
nutrients = ['Total Fat (g)', 'Sugars (g)', 'Protein (g)', 'Caffeine (mg)']
st.header('Análisis Nutricional de las Bebidas')
selected_nutrient = st.selectbox('Selecciona un Nutriente', nutrients)
fig2 = px.scatter(beverages, x='Beverage', y=selected_nutrient, color='Beverage_category')
st.plotly_chart(fig2, use_container_width=True)


# calorias por tipo de leche
# Calculando la media de calorias por tipo de leche (Beverage_prep)
calorie_means = df.groupby('Beverage_prep')['Calories'].mean().reset_index()

# Crear un gráfico de barras
fig4 = px.bar(calorie_means, x='Beverage_prep', y='Calories', title='Media de Calorías por Tipo de Leche',
              color='Calories', color_continuous_scale='greens')

# Mostrar el gráfico
st.header('Calorías por tipo de leche')
st.plotly_chart(fig4, use_container_width=True)


# Grafico circular
# Contar el número de bebidas por tipo
beverage_counts = df['Beverage_category'].value_counts().reset_index()
beverage_counts.columns = ['Beverage_category', 'Count']

# Crear un gráfico circular
fig5 = px.pie(beverage_counts, names='Beverage_category', values='Count', title='Número de Bebidas por Tipo de Bebida')

# Mostrar el gráfico
st.header('Valores nutricionales por tipo de bebida')
st.plotly_chart(fig5, use_container_width=True)


# sodio en bebidas
st.header('Sodio en bebidas')
# Slider para seleccionar el rango de sodio
min_sodium, max_sodium = st.slider('Selecciona el rango de sodio (mg)', 
                                   int(df['Sodium (mg)'].min()), 
                                   int(df['Sodium (mg)'].max()), 
                                   (0, 50))

# Filtrar datos según el rango de sodio seleccionado
filtered_df = df[(df['Sodium (mg)'] >= min_sodium) & (df['Sodium (mg)'] <= max_sodium)]

# Crear un gráfico de barras
fig7 = px.bar(filtered_df, x='Beverage', y='Sodium (mg)', 
             color='Beverage_category', 
             title='Bebidas de Starbucks por Contenido de Sodio')

# Mostrar el gráfico
st.plotly_chart(fig7)

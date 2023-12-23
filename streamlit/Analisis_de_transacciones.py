
import streamlit as st
import time

from pages import  Historia, Analisis, Feedback

st.set_page_config(page_title='Starbucks Analysis', layout='wide',     page_icon="☕")
# Encabezado principal
st.image('starbuckslogo.png')
st.title('ESTUDIO BEBIDAS STARBUCKS')

# st.sidebar.success("Selecciona la única página que te voy a dejar seleccionar. Eres libre de seleccionar.")

st.markdown(
    """
    Starbucks, con su renombre como una de las empresas líderes en el ámbito de las cafeterías a nivel mundial, ofrece una amplia gama de cafés 
    y bebidas que se han convertido en una parte esencial de la cultura urbana moderna. Este proyecto se enfoca en realizar un análisis 
    exhaustivo de las bebidas servidas por Starbucks, con el objetivo de descubrir no solo la diversidad y riqueza de su oferta sino también 
    para evaluar las propiedades nutricionales de estas bebidas. El análisis pretende ser una herramienta clave para aquellos que buscan hacer 
    elecciones informadas sobre su consumo de bebidas, especialmente desde un punto de vista de salud y necesidades dietéticas específicas.

    La base de datos que se analizará en este proyecto es una colección detallada de las diferentes bebidas ofrecidas por Starbucks. 
    Cada entrada en la base de datos no solo clasifica la bebida en un tipo específico, como café, té, infusiones, entre otros, sino que 
    también proporciona información detallada sobre su composición nutricional. Esto incluye, pero no se limita a, contenido calórico, 
    niveles de grasas (saturadas y trans), azúcares, proteínas, y otros elementos que son de interés para aquellos preocupados por su 
    ingesta nutricional.

    La práctica os la voy a evaluar del siguiente modo:
    
    1. Para tener un apto (5) deberéis buscar un conjunto de datos, documentarlo, y hacer un dashboard. La nota puede llegar a 6 en función de 
       que lo que me quieras contar se entienda bien con el dashboard que me muestras. 
    2. Para llegar al 7, deberá tener gráficos de tipo interactivos.
    3. Para llegar al 8, en el backend deberá tener un método post, que tenga sentido.
    4. Para llegar al 9, deberás utilizar una jerarquía de clases con BaseModel y, además, hacer una adecuada gestión de errores: excepciones y logs.
    5. Para llegar al 10, deberías utilizar una base de datos en un servicio adicional. 
    6. Me haría muy feliz si utilizaseis un ORM como SQLAlchemy.
   
    A por ello! 💪💪💪
"""
)


# Muestra la página seleccionada
#page = pages[selected_page]
#page.app()
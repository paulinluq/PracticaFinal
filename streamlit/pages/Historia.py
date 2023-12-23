import streamlit as st
st.set_page_config(page_title='Historia Starbucks ', layout='wide',     page_icon="☕")
# Encabezado principal
st.title('*HISTORIA BEBIDAS STARBUCKS*')

# Columnas para Introducción
col1, col2 = st.columns([3, 2])
with col1:
    st.header("Introducción")
    st.write("""
        Desde sus humildes comienzos en las calles empedradas de Seattle hasta convertirse en un gigante global, Starbucks ha redefinido la experiencia
        del café para millones de personas en todo el mundo. Fundada en 1971, esta compañía no solo ha transformado cómo el mundo consume café, 
        sino que también ha establecido un nuevo paradigma en la cultura del café y el marketing de marca.
    """)
with col2:
    st.image("starbuckslogo.png", width=200)  

# Columnas para Cimientos y Primeros Años (1971-1980s)
col3, col4 = st.columns([2, 3])
with col4:
    st.header("Cimientos y Primeros Años (1971-1980s)")
    st.write("""
        Starbucks comenzó como una pequeña tienda en Seattle, fundada por Jerry Baldwin, Zev Siegl y Gordon Bowker. 
    Inspirándose en el personaje de "Starbuck" de "Moby-Dick", inicialmente se centró en la venta de granos de café de alta calidad y equipos
    para hacer café. Fue la incorporación de Howard Schultz en 1982 lo que marcó un punto de inflexión para Starbucks. 
    Schultz, después de un viaje a Italia y fascinado por las cafeterías italianas, vislumbró un futuro diferente para Starbucks, 
    no solo como un vendedor de café sino como una experiencia completa de cafetería.
    """)
with col3:
    st.image("starbucks1971.jpg")  

st.header("Transformación y Expansión Nacional (1980s-1990s)")
st.write("""
        En 1987, Schultz adquirió Starbucks y comenzó a transformarla en una cadena de cafeterías. 
    Introduciendo cafés al estilo italiano como espresso y cappuccino, Schultz quería que Starbucks fuera un "tercer lugar" entre el hogar y 
    el trabajo para los clientes. Durante este período, Starbucks experimentó un crecimiento exponencial, expandiéndose primero a través de 
    Estados Unidos y luego, en la década de 1990, comenzando su aventura global.
    """)


col5, col6 = st.columns([1, 1])
with col5:
    st.header("Era de Globalización y Diversificación (2000s-Presente)")
    st.write("""
        En el siglo XXI, Starbucks no solo continuó su expansión geográfica sino que también diversificó su oferta. 
    Con la adquisición de Teavana, la introducción de bebidas frías y opciones de alimentos, Starbucks amplió su menú para atraer a un público
    más amplio. Además, la adopción de tecnologías como aplicaciones móviles para pedidos y pagos reflejó su adaptación a la era digital.
    Durante este tiempo, Starbucks también enfrentó críticas y desafíos, incluyendo cuestiones de sostenibilidad y prácticas comerciales.
    """)
with col6:
    st.image("starbucksglobalizacion.jpeg", width=350)  

st.header("Impacto Cultural y Legado")
st.write("""
        Más que una cadena de cafeterías, Starbucks se ha convertido en un ícono cultural. Ha redefinido cómo las personas perciben el café, 
    transformándolo de una mera bebida a una experiencia rica y personal. Con su ambiente acogedor y su enfoque en la sostenibilidad y 
    responsabilidad social, Starbucks ha establecido nuevos estándares en el mundo del café. Sin embargo, no está exento de controversias y 
    desafíos, especialmente en lo que respecta a sus prácticas comerciales y ambientales.
    """)
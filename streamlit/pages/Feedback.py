
import streamlit as st
import requests

st.set_page_config(page_title='Starbucks Analysis', layout='wide', page_icon="☕")
st.title("Feedback de Bebidas Starbucks")

with st.form("feedback_form"):
    page_name = st.selectbox("¿Sobre qué página te gustaría enviar feedback?", ["Starbucks", "Análisis", "Historia"])
    rating = st.slider("Califica esta página (1 = Mala, 5 = Excelente)", 1, 5, 3)
    feedback = st.text_area("Tu Feedback")
    submitted = st.form_submit_button("Enviar Feedback")

    if submitted:
        response = requests.post(
            "http://localhost:5000/submit_feedback",
            json={"pagina": page_name, "calificacion": rating, "feedback": feedback}
        )
        if response.status_code == 200:
            st.success("¡Feedback enviado con éxito!")
        else:
            st.error("Hubo un problema al enviar el feedback.")

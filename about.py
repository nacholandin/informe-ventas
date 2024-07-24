import streamlit as st


def about_app():

    st.header("ABOUT ME")

    st.write("Este proyecto es una muestra de los conocimientos y capacidad para realizar tipo de analisis y presentación de los resultados obtenidos. Para conocer más sobre mi y otros proyectos realizados te invito a visitar mi Linkedin o Github donde podras conocer más y ver mas proyectos. ")

    col1, col2 = st.columns([3, 1])


    with col1:
        st.markdown(
        "Ignacio Landín García: Junior Data Scientist | Especialista en Inteligencia Artificial, Python, SQL y Machine Learning | Contable."
    )

    with col2:
    
        if st.button('LinkedIn', key='button_linkedin'):
            st.markdown(
            '<a href="https://www.linkedin.com/in/ignacio-landin-garcia" target="_blank"><button>Perfil LinkedIn</button></a>',
            unsafe_allow_html=True
        )
    

        if st.button('GitHub', key='button_github'):
            st.markdown(
            '<a href="https://github.com/nacholandin" target="_blank"><button>Perfil GitHub</button></a>',
            unsafe_allow_html=True
        )

if __name__ == "__about_app__":
    about_app()
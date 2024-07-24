import streamlit as st
import plotly.express as px
from module.aplication import *
from eda import eda_app
from about import about_app

 
def main():
    st.set_page_config(**PAGE_CONFIG)
   
    menu = ["Home", "Exploratory Data Analysis", "About me"]

    choice = st.sidebar.selectbox(label = "Menu", options = menu, index = 0)
 
    if choice == "Home":
        #image = Image.open("source/Red and Blue Movie Night Poster (3).png")
        #st.image(image           = image,
                   #width=500)
        #     #   use_column_width = True#)
        
        st.header(body = "Introducción")

        st.subheader("Proyecto Analisis de ventas de 5 tiendas diferentes")

        
        


    elif choice == "Exploratory Data Analysis":
        eda_app()

    else:
        about_app()

if __name__ == "__main__":
    main()
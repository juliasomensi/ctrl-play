import streamlit as st

st.set_page_config(page_title= "Dia das mães", page_icon="👩‍👦")

st.title("FELIZ DIA DAS MÃES!")
nome = st.text_input("Digite o nome da sua mãe: ")

if st.button("Mostrar mensagem"):
    if nome:
        st.success(f"{nome}, você é a melhor mãe do mundo, te amo! ❤")
        st.balloons()
    else:
        st.warning("Digite o nome da sua mãe para ver a homenagem!")

st.image("", use_container_width= True)
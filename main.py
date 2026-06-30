import streamlit as st
from summarization import resumir_texto

def main():
    st.header("Chatbot Simples", divider = True, text_alignment = "center")
    st.markdown("Selecione a IA que mais vai te ajudar, envie seu prompt e seja feliz!")

    opcoes = ["Gerar Texto", "Resumir Texto", "Abrir Chat"]
    opcao_selecionada = st.selectbox("Selecione a ferramenta desejada: ", options = opcoes)

    if opcao_selecionada:
        prompt_usuario = st.chat_input("Digite seu prompt aqui: ")

        if opcao_selecionada == opcoes[0] and prompt_usuario:
            pass
        elif opcao_selecionada == opcoes[1] and prompt_usuario:
            resumir = resumir_texto(prompt_usuario)
            st.write(resumir)
        elif opcao_selecionada == opcoes[2] and prompt_usuario:
            pass
        
if __name__ == "__main__":
    main()
import streamlit as st
from summarization import resumir_texto
from generation import gerar_texto
from chat_completion import completar_chat

def main():
    st.header("Chatbot Simples", divider = True, text_alignment = "center")
    st.markdown("Selecione a IA que mais vai te ajudar, envie seu prompt e seja feliz!")

    opcoes = ["Gerar Texto", "Resumir Texto", "Abrir Chat"]
    opcao_selecionada = st.selectbox("Selecione a ferramenta desejada: ", options = opcoes)

    if opcao_selecionada:
        prompt_usuario = st.chat_input("Digite seu prompt aqui: ")
        
        if prompt_usuario:
          if opcao_selecionada == opcoes[0]:
              texto = gerar_texto(prompt_usuario)
              st.write(texto)
          elif opcao_selecionada == opcoes[1]:
              resumo = resumir_texto(prompt_usuario)
              st.write(resumo)
          elif opcao_selecionada == opcoes[2]:
              if "mensagens" not in st.session_state:
                  mensagens = [
                      {"role": "system", "content": "Responda as perguntas de forma correta e precisa"}
                  ]
              else:
                  mensagens = st.session_state["mensagens"]

              mensagens.append({"role": "user", "content": prompt_usuario})
              mensagens = completar_chat(mensagens)
              st.session_state["mensagens"] = mensagens
              
              for mensagem in mensagens:
                  if mensagem["role"] != "system":
                      with st.chat_message(mensagem["role"]):
                          st.write(mensagem["content"])
        
if __name__ == "__main__":
    main()
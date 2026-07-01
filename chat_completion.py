from transformers import pipeline

modelo = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", device = "cuda")

def completar_chat(mensagens):
  resposta = modelo(mensagens, max_new_tokens=100)

  mensagens.append({"role": "assistant", "content": resposta[0]["generated_text"][-1]["content"]})

  return mensagens
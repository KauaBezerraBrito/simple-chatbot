from transformers import pipeline

modelo = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", device = "cuda")

def gerar_texto(prompt):
  mensagens = [
      {"role": "user", "content": prompt},
  ]

  resposta = modelo(mensagens, max_new_tokens=100)

  return resposta[0]["generated_text"][1]["content"]
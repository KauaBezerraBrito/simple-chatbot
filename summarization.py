from transformers import pipeline

modelo = pipeline("summarization", model="facebook/bart-large-cnn", device = "cuda")

def resumir_texto(prompt):
    resposta = modelo(prompt)

    return resposta[0]["summary_text"]
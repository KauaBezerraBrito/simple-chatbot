from transformers import pipeline

modelo = pipeline("summarization", model="facebook/bart-large-cnn", device = "cuda")

def resumir_texto(prompt):
    resposta = modelo(prompt, max_length=130, min_length=30, do_sample=False)

    return resposta[0]["summary_text"]
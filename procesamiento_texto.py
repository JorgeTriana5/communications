# procesamiento_texto.py
import spacy

class ProcesadorTexto:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def extraer_palabras_clave(self, texto):
        doc = self.nlp(texto)
        palabras_clave = []
        for token in doc:
            if not token.is_stop and not token.is_punct:
                palabras_clave.append(token.lemma_.lower())
        return palabras_clave


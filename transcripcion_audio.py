# transcripcion_audio.py
import speech_recognition as sr

class TranscriptorAudio:
    def __init__(self):
        self.reconocedor = sr.Recognizer()

    def transcribir_audio(self, source):
        print("Escuchando...")

        # Comenzar a grabar
        audio = self.reconocedor.listen(source)

        # Transcribir el audio grabado
        texto_transcrito = self.reconocedor.recognize_google(audio, language="es-ES")

        # Mostrar el texto transcribido
        print("Texto transcrito:", texto_transcrito)

        return texto_transcrito

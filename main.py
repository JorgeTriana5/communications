# main.py
import speech_recognition as sr
from transcripcion_audio import TranscriptorAudio
from procesamiento_texto import ProcesadorTexto
from response import Response, response


def main():
    transcriptor = TranscriptorAudio()
    procesador = ProcesadorTexto()

    try:
        # Utilizar el micrófono como fuente de audio
        with sr.Microphone() as source:
            # Transcribir el audio
            texto_transcrito = transcriptor.transcribir_audio(source)

            # Procesar el texto y extraer palabras clave
            palabras_clave = procesador.extraer_palabras_clave(texto_transcrito)

            # Mostrar las palabras clave
            print("Palabras clave:", palabras_clave)

            # Encontrar la mejor respuesta
            best_response = response.find_response(texto_transcrito)
            print("Respuesta robot:", best_response)

    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio.")
    except sr.RequestError as e:
        print(f"No se pudo solicitar resultados desde el servicio de Google Speech Recognition: {e}")

if __name__ == "__main__":
    main()


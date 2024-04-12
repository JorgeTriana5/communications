import csv

class Response:
    def __init__(self, csv_file):
        self.conversations = self.load_conversations(csv_file)

    def load_conversations(self, csv_file):
        conversations = []
        with open(csv_file, 'r', encoding='latin1') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                conversations.append(row)
        return conversations

    def find_response(self, input_text):
        input_keywords = set(input_text.lower().split())

        best_response = None
        max_matches = 0

        for human_input, robot_response in self.conversations:
            conversation_keywords = set(human_input.lower().split())

            # Calcular la cantidad de palabras clave coincidentes
            matches = len(input_keywords.intersection(conversation_keywords))

            # Actualizar la mejor respuesta si hay más coincidencias
            if matches > max_matches:
                max_matches = matches
                best_response = robot_response

        return best_response

# Uso del código
csv_file = "conversaciones.csv"
response = Response(csv_file)



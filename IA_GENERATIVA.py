import openai                               
import os

# Configura tu clave de API de OpenAI
openai.api_key = '' #esta es una clave personal, no puede ser transferida. Para que funcione el codigo solicita tu propia clave en la pagina de OpenAI

# Funcion para generar respuestas usando GPT-3.5-turbo
def generateResponse(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message['content']

# Funcion para cargar el contenido de un documento
def loadDocument(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Funcion para mostrar el menu y obtener la opcion del usuario
def show_menu():
    print("\nGenerador de Respuestas con IA")
    print("1) Cargar nuevo documento para analizar")
    print("2) Ingresar pregunta")
    print("3) Salir del generador")
    return input("Selecciona una opcion: ")

# Funcion principal del programa
def main():
    documentCount = 0
    documents = []
    messages = [
        {"role": "system", "content": "You are a helpful assistant skilled in providing detailed answers based on provided documents."}
    ]

    while True:
        option = show_menu()

        if option == '1':
            if documentCount >= 5:
                print("No se pueden cargar mas de 5 documentos.")
                continue

            file_path = input("Ingresa la ruta del documento: ")
            if os.path.exists(file_path):
                documentContent = loadDocument(file_path)
                documents.append(documentContent)
                documentCount += 1
                print(f"Documento cargado. Total de documentos: {documentCount}")
            else:
                print("La ruta del documento no es valida.")

        elif option == '2':
            if documentCount < 3:
                print("Debes cargar al menos 3 documentos antes de hacer una pregunta.")
                continue

            question = input("Ingresa tu pregunta: ")
            questionMessage = {"role": "user", "content": question}

            # Combina los documentos y la pregunta para generar una respuesta
            combinedMessages = messages + [{"role": "user", "content": doc} for doc in documents] + [questionMessage]
            response = generateResponse(combinedMessages)
            print("\nRespuesta generada por la IA:\n")
            print(response)

        elif option == '3':
            print("Saliendo del generador...")
            break

        else:
            print("Opcion no valida. Por favor, selecciona una opcion valida.")

if __name__ == "__main__":
    main()

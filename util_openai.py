from openai import OpenAI

def organizar_directorio(api, prompt):
    client = OpenAI(
        api_key=api,
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system", 
                "content": """Tu trabajo como asistente es tomar una lista de clasificaciones 
                de directorios, y a partir de otra lista de nombres de directorios, clasificar 
                cada uno de ellos a uno de los directorios otorgados en la lista anterior. Devuelvelo 
                como formato de diccionario siendo la clave la clasificacion del directorio con una
                sola palabra que diga clasificaciones, y el valor una lista con los nombres de
                directorios correspondientes. La clave raiz de tu respuesta SIEMPRE debe ser solamente una
                palabra. Siempre debes utilizar todas las clasificaciones
                otorgadas aunque el contenido del diccionario este vacio para esa clave.
                En caso de que no exista una clasificacion para el nombre del archivo, excluirlo 
                del diccionario. SIEMPRE devuelve unicamente un diccionario de python llamado 
                clasificaciones que contenga el contenido pedido anteriormente. 
                NUNCA generes una nueva clasificacion ni nombre de archivo que no 
                haya sido otorgado por el usuario. Debes devolver un formato compatible para convertir en
                JSON, es decir, que funcione con json.loads"""},
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo-1106",
    )
    return chat_completion.choices[0].message.content
import json
import requests

Token = "1623948894:AAEPSfMTtW7q9mu96Y-7Ftvdl5JkYtEsj9c"
Url = "https://api.telegram.org/bot"+ Token +"/"

def update(offset):
    respuesta = requests.get(Url + "getUpdates" + "?offset=" + str(offset) + "&timeout=" + str(100))
    mensajes_js = respuesta.content.decode("utf8")
    mensajes_diccionario = json.loads(mensajes_js)
    return mensajes_diccionario

def leer_mensajes(mensajes):
    texto = mensajes["message"]["text"]
    persona = mensajes["message"]["from"]["first_name"]
    id_chat = mensajes["message"]["chat"]["id"]
    id_update = mensajes["update_id"]
    
    return id_chat, persona, texto, id_update

def enviar_mensaje(idchat, texto):
    requests.get(Url + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))

ultima_id = 0 

while True:
 mensajes_diccionario = update(ultima_id)
 for i in mensajes_diccionario["result"]:
     
    id_chat, persona, texto, id_update = leer_mensajes(i)
    
    if id_update > (ultima_id-1):
            ultima_id = id_update + 1
            
    if "Hola" or "Hola!" or "hola" or "¡Hola!" in texto:
        msj_respuesta = "¡Hola, " + persona + "! \nSoy un bot que monitorea los sensores de temperatura y presión."
        
    elif "Adiós" or "adiós" or "Adiós!" or "¡Adiós!" in texto:
        msj_respuesta="¡Hasta pronto! :)"
        
    enviar_mensaje(id_chat, msj_respuesta)
    
 mensajes_diccionario = []
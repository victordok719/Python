import time
import openai

key="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"
#Enter your OpenAI API key here.
openai.api_key=key


preguntas=list()    #Lista de preguntas
respuestas=list()   #Lista de respuestas
mensajes=list()     #Lista de mensajes 


contexto=input("Sistema: En que contexto quieres profundizar: ")
if contexto =="":
    contexto="Responde mas claro por favor: "

mensajes.append({"role":"system", "content": contexto})


while True:
    pregunta_actual=input("Yo: ")
    if pregunta_actual.lower() in ['exit','quit','parar','stop','alto','salir', 'bye']:
        print("Chatbot: Fue un placer ayudarte...!")
        time.sleep(5)
        ##Tiempo para cerrar el programa
        break
    if pregunta_actual=="":
        continue

    mensajes.append({"role":"user","content":pregunta_actual})
    respuestas=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        temperature=0.7,
        #max_tokens=500,
    )

    respuesta_actual=respuestas.choices[0]['messages']['content']
    print(f'\nChatbot: {respuesta_actual}')

    respuestas_gpt.append(respuesta_actual)


    mensajes.append({"role":"assistant","content":respuestas_gpt})
    print()
    print("*"*150)
    print()


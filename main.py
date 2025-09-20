from openai import OpenAI
import json
from fastapi import FastAPI, Form, Request, Response, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated

with open('api_key.json', 'r') as apikey_file:
    data=json.load(apikey_file)
    api_key=data['api_key']


#create openai object
bot=OpenAI(
    api_key=api_key
)


#create template
template=Jinja2Templates(directory='templates')


#create app with fastapi
app=FastAPI()

#initialize chatBot history
chatBot_messages=[
    {
        'role':'system',
        'content':'you are a micro electronic assistant'
    }
]
chat_history=[]

#create post method
@app.post('/', response_class=HTMLResponse)
async def chat_post(request:Request, user_input:str=Form()):

    #append to chatBot history user input
    chatBot_messages.append(
        {
            'role':'user',
            'content':user_input
        }
    )
    chat_history.append(user_input)

    response=bot.chat.completions.create(
        model='chatgpt-4o-latest',
        temperature=1.0,
        messages=chatBot_messages
    )

    #take only assistant response
    chatBot_response=response.choices[0].message.content

    chat_history.append(chatBot_response)

    #append to chatBot assistant response
    chatBot_messages.append(
        {
            'role':'assistant',
            "content":chatBot_response
        }
    )

    return template.TemplateResponse(request=request, name='home.html', context={'chatBot_messages':chat_history})


#create get method to land to page first time
@app.get('/ws', response_class=HTMLResponse)
async def chatBot(request:Request):
    return template.TemplateResponse(name='home.html', request=request)


@app.websocket('/ws')
async def chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        user_input= await websocket.receive_text()
        await websocket.send_text(user_input)    
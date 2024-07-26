from socketio import ASGIApp, AsyncServer
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

sio = AsyncServer( cors_allowed_origins="*", async_mode='asgi')

socket_app = ASGIApp(sio)

app.mount('/socket.io', app=socket_app)

@app.get("/")
def home():
    return "hello"

@sio.event
async def connect( sid, env):
    print("New client:" + str(sid))

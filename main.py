from fastapi import FastAPI
from fastapi_socketio import SocketManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI( )
app.add_middleware( CORSMiddleware, allow_origins=["*"])
io = SocketManager( app=app, cors_allowed_origins="*" )

@app.sio.on('connect')
async def connect( sid, environ ):
    print('conectado')
    print("conectado:" + sid )
    await io.emit('message', 'Bienvenido', to= io )


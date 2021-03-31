from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumer

websocketURLs=[
    path('ws/chat/<slug:room_name>',consumer.Chatconsumer.as_asgi())

]
application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(websocketURLs))
})
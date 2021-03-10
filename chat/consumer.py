from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random
from .models import Message
from channels.db import database_sync_to_async



class Chatconsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def add_msg(self,message):
        print("here")
        msg=Message(sender=self.user,message=message,chat_room_id=self.groupname)
        
        msg.save()

    async def connect(self):
        self.groupname=self.scope['url_route']['kwargs']['room_name']
        print(self.groupname)
        self.user=self.scope['user']
        print(self.user)
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
        
    
    async def receive(self,text_data):
        data=json.loads(text_data)
        message=data['message']
        sender="keval"
        r1 = random.randint(0, 10) 
        if r1%2==0:
            sender="jenil"
        await self.add_msg(message)
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'handle_message',
                'message':{
                    'sender':self.user.username,
                    'message':message
                }
            }
        )
        

    async def handle_message(self,event):
        messages=event['message']['message']
        sender=event['message']['sender']
        print(sender)
        
        await self.send(text_data=json.dumps({'message':messages,'sender':sender}))

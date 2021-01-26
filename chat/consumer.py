from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random

class Chatconsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.groupname='jenil_keval'
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

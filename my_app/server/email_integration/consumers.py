import json

from channels.generic.websocket import AsyncWebsocketConsumer


class EmailImportConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('email_import', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('email_import', self.channel_name)

    async def email_import_progress(self, event):
        message = event['message']
        progress = event['progress']
        await self.send(text_data=json.dumps({
            'type': 'progress',
            'message': message,
            'progress': progress
        }))

    async def email_import_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message
        }))

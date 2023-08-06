import json
from channels.generic.websocket import AsyncWebsocketConsumer
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            'notifications_group',
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'notifications_group',
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        notification_type = data.get('type')
        if notification_type == 'notification':
            message = data.get('message')
            await self.send_notification(message)

    async def send_notification(self, message):
        await self.send(json.dumps({
            'type': 'notification',
            'message': message
        }))

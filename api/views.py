from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class NotificationAPIView(APIView):
    def post(self, request):
        message = request.data.get('message')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifications_group',
            {
                'type': 'send_notification',
                'message': message
            }
        )
        return Response({'message': 'Notification sent successfully.'})
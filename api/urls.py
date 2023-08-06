from django.urls import path

from . import views


urlpatterns = [
  
    path('api/notifications/', views.NotificationAPIView.as_view(), name='notification-list'),
 
]
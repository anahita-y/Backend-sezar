from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self , serializer):
        instance = serializer.save()

        send_mail(subject = "f پیام جدیداز {instance.name} -{instance.topic}" ,
                   message = "f نام : {instance.name}\n ایمیل : {instance.email}\nموضوع : {instance.topic}\n\nمتن پیام : \n{instance.messageText}",
                    from_email = settings.DEFAULT_FROM_EMAIL, 
                    recipient_list = [settings.ADMIN_EMAIL] , 
                    fail_silently = True ,)

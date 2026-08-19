from django.db import models

class ContactMessage(models.Model):
    class Status(models.TextChoices):
        READ = "R" , "Read"
        UNREAD = "U" ,"Unread"

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    topic = models.CharField(max_length = 255)
    messageText = models.TextField()
    status = models.CharField(max_length = 1 , choices = Status.choices , default = Status.UNREAD) 
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
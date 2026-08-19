from django.db import models

class Experience(models.Model):
    class Status(models.TextChoices):
        COMPLETED = "C" , "Completed"
        IN_PROGRESS = "P" , "In progress"

    year = models.PositiveIntegerField()
    title = models.CharField(max_length = 255)
    short_description = models.TextField()
    image = models.ImageField(null = True , blank = True)
    status = models.CharField(max_length = 1 , choices = Status.choices , default = Status.IN_PROGRESS)

    def __str__(self):
        return self.title

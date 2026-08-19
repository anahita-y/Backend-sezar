from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 100)
    role_title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100 , blank = True)
    bio = models.TextField()
    is_available = models.BooleanField(default = True)
    availability_label = models.CharField(max_length = 100 , blank = True)

    def __str__(self):
        return self.name

class SiteDocument(models.Model):
    class DocType(models.TextChoices):
        RESUME = "R" , "Resume"
        CONTRACT = "C" ,"Contract"
        TARIFF = "T" , "Tariff"
        PACKAGES = "P" ,"Packages"

    doc_type = models.CharField(max_length = 1 , choices = DocType.choices , unique = True)
    title = models.CharField(max_length = 100)
    file = models.FileField(upload_to = 'documents/')

    def __str__(self):
        return self.title
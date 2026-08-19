from django.db import models

class SocialLink(models.Model):
    platform = models.CharField(max_length = 50)
    icon = models.CharField(max_length = 50)
    url_or_value = models.CharField(max_length = 255)
    label = models.CharField(max_length = 100 , blank = True)
    map_link = models.URLField(null = True , blank = True)

    def __str__(self):
        return self.platform
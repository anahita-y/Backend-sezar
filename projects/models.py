from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
       verbose_name_plural = "Technologies"
       
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length = 200)
    short_description = models.CharField(max_length = 400)
    technologies = models.ManyToManyField(Technology)
    image = models.ImageField()

    def __str__(self):
        return self.title



class ProjectDetail(models.Model):
    challenge = models.TextField()
    solution = models.TextField()
    result = models.TextField()
    demo_link = models.URLField(null = True , blank = True)
    project = models.OneToOneField(Project, on_delete = models.CASCADE, related_name = 'detail')

    def __str__(self):
        return f"Detail for{self.project.title}"


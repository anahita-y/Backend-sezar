from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length = 50)
    icon = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.title

class SkillProof(models.Model):
    certificate = models.ImageField(null = True , blank = True)
    project = models.URLField(null = True , blank = True)
    skill = models.ForeignKey(Skill , on_delete = models.CASCADE , related_name = 'proofs')

    def __str__(self):
        return f"Proof for {self.skill.title}"

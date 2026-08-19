from django.contrib import admin
from .models import Skill, SkillProof

class SkillProofInline(admin.TabularInline):
    model = SkillProof
    extra = 1

class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillProofInline]

    
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillProof)

from django.contrib import admin
from .models import Skill, SkillProof

class SkillProofInline(admin.TabularInline):
    model = SkillProof
    extra = 1
    fields = ['certificate' , 'project']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title' , 'icon' , 'proofs_count']
    search_fields = ['title']
    inlines = [SkillProofInline]

    def proofs_count(self , obj):
        return obj.proofs.count()
    proofs_count.short_description = 'تعداد مدارک'


@admin.register(SkillProof)
class SkillProofAdmin(admin.ModelAdmin):
    list_display = ['skill', 'project' , 'has_certificate']
    list_filter = ['skill']

    def has_certificate(self , obj):
        return bool(obj.certificate)

    has_certificate.boolean = True
    has_certificate.short_description = 'مدرک دارد؟'


#admin.site.register(Skill, SkillAdmin)
#admin.site.register(SkillProof)

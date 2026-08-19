from django.contrib import admin
from .models import Project , ProjectDetail , Technology

class ProjectDetailInline(admin.StackedInline):
    model = ProjectDetail
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline]


admin.site.register(Project , ProjectAdmin)
admin.site.register(ProjectDetail)
admin.site.register(Technology)
from django.contrib import admin
from .models import Project , ProjectDetail , Technology
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



class ProjectDetailInline(admin.StackedInline):
    model = ProjectDetail
    extra = 1
    fields = ['challenge' , 'solution' , 'result' , 'demo_link']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title' , 'short_description' , 'display_technologies']
    filter_horizontal = ['technologies']
    inlines = [ProjectDetailInline]
    search_fields = ['title' , 'short_description']


    def display_technologies(self , obj):
        return "،".join([t.name for t in obj.technologies.all()])
    display_technologies.short_description = 'تکنولوژی'



@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ['project' , 'demo_link']
    search_fields = ['project__title']


#admin.site.register(Project , ProjectAdmin)
#admin.site.register(ProjectDetail)
#admin.site.register(Technology)
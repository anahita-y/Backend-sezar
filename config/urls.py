from django.contrib import admin 
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/" , admin.site.urls),
    path("api/home/" , include("home.urls")),
    path("api/projects/" , include("projects.urls")),
    path("api/skills/" , include("skills.urls")),
    path("api/experience/" , include("experience.urls")),
    path("api/contact/" , include("contactMessage.urls")),
    path("api/social/" , include("sociallink.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
# from django.contrib import admin
# from django.conf.urls import url
# from django.urls import path
# from Home_Coaching import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve


# urlpatterns = [
#     path("", views.index, name='index'),
#     path("singup", views.singup, name='singup'),
#     path("login", views.loginUser, name='loginuser'),
#     path("logout", views.logout, name='logout'),
#     path("home", views.home, name='home'),
#     path("demo", views.demo, name='demo'),
#     path("notes", views.notes, name='notes'),
#     path(r'^download/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
#     path("feedback", views.feedback, name='feedback'),
#     path("upload-notes", views.uploadnotes, name='upload-notes'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
       
from django.contrib import admin
from django.urls import path
from Home_Coaching import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("", views.index, name='index'),
    path("singup", views.singup, name='singup'),  # Corrected the typo in the path
    path("login", views.loginUser, name='loginUser'),  # Corrected the function name to follow PEP 8 conventions
    path("logout", views.logout, name='logout'),  # Corrected the function name to follow PEP 8 conventions
    path("home", views.home, name='home'),
    path("about", views.about, name='about'),
    path("demo", views.demo, name='demo'),
    path("feedback", views.feedback, name='feedback'),
    
    path("notes", views.notes, name='notes'),
    path("download/<path:path>", serve, {'document_root': settings.MEDIA_ROOT}),
    path("uploadnotes", views.uploadnotes, name='uploadnotes'),  # Corrected the function name to follow PEP 8 conventions
    
    path("courses", views.courses, name='courses'),
    path("download/<path:path>", serve, {'document_root': settings.MEDIA_ROOT}),
    path("uploadcourses", views.uploadcourses, name='uploadcourses'),  # Corrected the function name to follow PEP 8 conventions
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from django.contrib import admin
from Home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^AddStory.html/', views.showStory, name='index'),
    url(r'^Home.html/', views.index, name='index'),
    url(r'^Details.html/', views.detail, name='index'),
    url(r'^About.html/', views.openAbout, name='index'),
    url(r'^$', views.openWelcome, name='index')
]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Storify_database
from .forms import UsernameForm, StoryForm
import datetime

# Variable for storing username
username = ""


def index(request):
    template = loader.get_template('Home.html')
    title_list = Storify_database.objects.values_list('category','title','writer','synopsis')
    context = {'title_list':title_list,'username':username}
    return HttpResponse(template.render(context, request))


def showStory(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        storify_db = Storify_database(title=form['TitleTextbox'].value(),category=request.POST.get("CategoryTextbox"),synopsis=form['SynopsisTextbox'].value(),writer=username,content=form['ContentTextbox'].value())
        storify_db.save()
        template = loader.get_template('Home.html')
        title_list = Storify_database.objects.values_list('category', 'title', 'writer', 'synopsis')
        context = {'title_list': title_list, 'username': username}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('AddStory.html')
        context = {'username':username}
        return HttpResponse(template.render(context, request))


def openWelcome(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        global username
        username = form['UsernameTextbox'].value()
        template = loader.get_template('Home.html')
        title_list = Storify_database.objects.values_list('category','title','writer','synopsis')
        context = {'title_list':title_list,'username': username}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('Welcome.html')
        context = {}
        return HttpResponse(template.render(context, request))


def detail(request):
    template = loader.get_template('Details.html')
    title_list = Storify_database.objects.get(synopsis=request.GET.get('query_name'))
    context = {'title_list':title_list,'username':username}
    return HttpResponse(template.render(context, request))


def openAbout(request):
    template = loader.get_template('About.html')
    context = {}
    return HttpResponse(template.render(context, request))

from django.http import Http404
from django.shortcuts import render
from manager.models import Home, MainContent, ContactUs, Service, OurProcess, SocialMedia, Client, Project


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"

    try:
        home_page = Home.objects.get(language='en')
    except Home.DoesNotExist:
        raise Http404("Home does not exist")

    try:
        main_content = MainContent.objects.get(language='en')
    except MainContent.DoesNotExist:
        raise Http404("Content does not exist")

    try:
        process_steps = OurProcess.objects.all()
    except OurProcess.DoesNotExist:
        raise Http404("Process informations do not exist")

    try:
        clients = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404("Clients informations do not exist")

    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404("Projects informations do not exist")

    try:
        socials_media = SocialMedia.objects.all()
    except SocialMedia.DoesNotExist:
        raise Http404("Socials media do not exist")

    try:
        contact_us = ContactUs.objects.all()
    except ContactUs.DoesNotExist:
        raise Http404(" performances do not exist")

    context = {
        'home_page': home_page,
        'main_content': main_content,
        'process_steps': process_steps,
        'partners': partners,
        'clients': clients,
        'projects': projects,
        'socials_media': socials_media,
        'contact_us': contact_us,

    }

    return render(request, url, context)

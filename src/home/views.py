from django.http import Http404
from django.shortcuts import render
from manager.models import Home, MainContent, ContactUs, Service, OurProcess, SocialMedia, Client, Project, TeamMember


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"

    context = {}

    return render(request, url, context)

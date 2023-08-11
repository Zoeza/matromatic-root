from django.http import Http404
from django.shortcuts import render
from .models import TopPage, Content, Service, OurProcess, Partner, SocialMedia, \
    Footer, Client, Project, Performance


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"

    try:
        top_page = TopPage.objects.get(language='en')
    except TopPage.DoesNotExist:
        raise Http404("Top page does not exist")

    try:
        content = Content.objects.get(language='en')
    except Content.DoesNotExist:
        raise Http404("Content does not exist")

    try:
        footer = Footer.objects.get(language='en')
    except Footer.DoesNotExist:
        raise Http404("Footer informations do not exist")

    try:
        services = Service.objects.all()
    except Service.DoesNotExist:
        raise Http404("Services informations do not exist")

    try:
        processes = OurProcess.objects.all()
    except OurProcess.DoesNotExist:
        raise Http404("Process informations do not exist")

    try:
        partners = Partner.objects.all()
    except Partner.DoesNotExist:
        raise Http404("Partners informations do not exist")

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
        performances = Performance.objects.all()
    except Performance.DoesNotExist:
        raise Http404(" performances do not exist")

    context = {
        'top_page': top_page,
        'content': content,
        'footer': footer,
        'services': services,
        'processes': processes,
        'partners': partners,
        'clients': clients,
        'projects': projects,
        'socials_media': socials_media,
        'performances': performances,

    }

    return render(request, url, context)


def contact_us(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/contact_us.html"
    return render(request, url, {})

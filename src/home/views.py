from django.http import Http404
from django.shortcuts import render
from .models import Header, Main, Service, OurProcess, Partner, SocialMedia, BackgroundImage, Footer, Client


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"

    try:
        header = Header.objects.get(sku='en')
    except Header.DoesNotExist:
        raise Http404("Top page does not exist")

    try:
        main = Main.objects.get(sku='en')
    except Main.DoesNotExist:
        raise Http404("Main informations do not exist")

    try:
        footer = Footer.objects.get(sku='en')
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
        socials_media = SocialMedia.objects.all()
    except SocialMedia.DoesNotExist:
        raise Http404("Socials media do not exist")

    try:
        background_images = BackgroundImage.objects.all()
    except BackgroundImage.DoesNotExist:
        raise Http404("Background images do not exist")

    context = {
        'header': header,
        'main': main,
        'footer': footer,
        'services': services,
        'processes': processes,
        'partners': partners,
        'clients': clients,
        'socials_media': socials_media,
        'background_images': background_images,

    }

    return render(request, url, context)

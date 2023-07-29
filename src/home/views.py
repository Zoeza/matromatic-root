from django.http import Http404
from django.shortcuts import render
from .models import Header, SocialMedia, BackgroundImage, Body


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"

    try:
        profile = Header.objects.get(sku='en')
    except Header.DoesNotExist:
        raise Http404("Top page does not exist")

    try:
        body = Body.objects.get(sku='en')
    except Header.DoesNotExist:
        raise Http404("Body informations do not exist")

    try:
        socials_media = SocialMedia.objects.all()
    except Header.DoesNotExist:
        raise Http404("Social media do not exist")

    try:
        background_images = BackgroundImage.objects.all()
    except Header.DoesNotExist:
        raise Http404("Background images do not exist")

    context = {
        'profile': profile,
        'body': body,
        'socials_media': socials_media,
        'background_images': background_images,

    }
    
    return render(request, url, context)

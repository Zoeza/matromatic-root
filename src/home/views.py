from django.http import Http404
from django.shortcuts import render
from .models import Header,SocialMedia


def home(request, ):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"
    try:
        profile = Header.objects.get(sku='en')
        socials_media = SocialMedia.objects.all()
    except Header.DoesNotExist:
        raise Http404("Top page does not exist")
    context = {
        'profile': profile,
        'socials_media': socials_media,

    }

    return render(request, url, context)

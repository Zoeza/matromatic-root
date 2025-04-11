from django.http import Http404
from django.shortcuts import render


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/index.html"

    context = {
        'page': {
            'menu_list': [
                ('home', "Acceuil"),
                ("about_us", "À propos de nous"),
                ("services", "Services"),
                ("projects", "Projets"),
                ("contact", "Contact")
            ]
        }
    }

    return render(request, url, context)

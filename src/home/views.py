from django.http import Http404
from django.shortcuts import render
import json
import os

def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/index.html"
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            page_data = json.load(file)
    except FileNotFoundError:
        raise Http404("Fichier JSON introuvable.")
    except json.JSONDecodeError:
        raise Http404("Erreur de lecture JSON.")

    context = {
        'page': {
            'menu_list': [
                ('home', "Accueil"),
                ('about_us', "À propos de nous"),
                ('services', "Services"),
                ('projects', "Projets"),
                ('contact', "Contact")
            ]
        },
        'data': page_data  #
    }

    return render(request, url, context)

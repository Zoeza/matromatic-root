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

        # Initialiser les compteurs de clics pour chaque projet
    for project_id in range(1, len(page_data['projects']['realizations']) + 1):
        if f'clickCount_project_{project_id}' not in request.session:
            request.session[f'clickCount_project_{project_id}'] = 0

        # Gérer le clic sur un projet
        if request.method == 'POST' and 'project_id' in request.POST:
            project_id = request.POST['project_id']
            if f'clickCount_project_{project_id}' in request.session:
                request.session[f'clickCount_project_{project_id}'] += 1
                request.session.modified = True  # Assurer que la session soit modifiée

        # Passer les données des projets avec les clics dans le contexte
        context = {
            'data': page_data,  # Passer les données JSON
            'projects': [
                {'id': project['id'], 'title': project['title'],
                 'click_count': request.session.get(f'clickCount_project_{project["id"]}', 0)}
                for project in page_data['projects']['realizations']
            ]
        }

        return render(request, url, context)

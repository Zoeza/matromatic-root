from django.shortcuts import render
from django.http import Http404
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

    # Vérification si des clics ont été effectués sur un projet
    if request.method == 'POST' and 'project_id' in request.POST:
        project_id = request.POST['project_id']

        # Assurer que le compteur de clics pour le projet existe dans la session
        if f'clickCount_project_{project_id}' not in request.session:
            request.session[f'clickCount_project_{project_id}'] = 0

        # Incrémenter le compteur de clics
        request.session[f'clickCount_project_{project_id}'] += 1
        request.session.modified = True  # Marque la session comme modifiée

    # Passer les projets avec les clics dans le contexte
    context = {
        'data': page_data,
        'projects': [
            {
                'id': project['id'],
                'title': project['title'],
                'img': project['img'],
                'click_count': request.session.get(f'clickCount_project_{project["id"]}', 0),
                'modal': project['modal']
            }
            for project in page_data.get('projects', {}).get('realizations', [])
        ]
    }

    return render(request, url, context)

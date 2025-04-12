from django.shortcuts import render,redirect
import json
import os
from django.http import Http404
from django.views.decorators.http import require_POST

def home(request):
    # Choix de langue
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'

    direction = request.session.get('language')
    url = direction + "/home/index.html"
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')

    # Charger les données du fichier JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            page_data = json.load(file)
    except FileNotFoundError:
        raise Http404("Fichier JSON introuvable.")
    except json.JSONDecodeError:
        raise Http404("Erreur de lecture JSON.")

    # Récupérer les compteurs de clics stockés en session (ou initialiser)
    click_counts = request.session.get("click_counts", {})

    # Injecter le compteur de clics dans chaque projet
    for project in page_data.get("projects", {}).get("realizations", []):
        project_id = str(project.get("id"))
        project["click_count"] = click_counts.get(project_id, 0)

    # Contexte envoyé au template
    context = {
        'data': page_data,
    }

    return render(request, url, context)


@require_POST
def increment_click(request):
    project_id = request.POST.get("project_id")
    if not project_id:
        raise Http404("ID du projet manquant.")

    # Lire les clics existants ou démarrer à 0
    click_counts = request.session.get("click_counts", {})
    click_counts[project_id] = click_counts.get(project_id, 0) + 1

    # Sauvegarder dans la session
    request.session["click_counts"] = click_counts

    return redirect("home")  # Redirige vers la vue d’accueil

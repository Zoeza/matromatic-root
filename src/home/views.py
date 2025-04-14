from django.shortcuts import render, redirect
import json
import os
from django.http import Http404
from django.views.decorators.http import require_POST


def home(request):
    # Vérifie si la langue est définie dans la session, sinon la définir à 'en-us'
    if not request.session.get('language'):
        request.session['language'] = 'en-us'

    direction = request.session['language']
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

    return render(request, url, {
        'data': page_data,
    })


def decrement_click(request):
    project_id = request.GET.get("project_id", '')
    if not project_id:
        raise Http404("ID du projet manquant.")

    click_counts = request.session.get("click_counts", {})
    selected_projects = request.session.get("selected_projects", [])

    current_count = click_counts.get(project_id, 0)

    if current_count > 1:
        click_counts[project_id] = current_count - 1
    else:
        # Si 1 ou moins : suppression du projet de la sélection
        click_counts.pop(project_id, None)
        if project_id in selected_projects:
            selected_projects.remove(project_id)

    request.session["click_counts"] = click_counts
    request.session["selected_projects"] = selected_projects
    request.session.modified = True  # Marquer la session comme modifiée

    return redirect("/?show_modal=true")


def project_modal_content(request, action):
    # Vérifie si la langue est définie dans la session, sinon la définir à 'en-us'
    if not request.session.get('language'):
        request.session['language'] = 'en-us'

    if "selected_projects" not in request.session:
        request.session["selected_projects"] = []

    direction = request.session['language']
    url = direction + "/home/partials/content.html"

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')

    # Charger les données du fichier JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            page_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise Http404("Erreur lors du chargement du fichier JSON.")

    # Obtenir tous les projets
    all_projects = page_data.get('projects', {}).get('realizations', [])

    selected_projects = request.session["selected_projects"]

    # Récupérer l'ID du projet depuis la requête
    project_id = request.GET.get("project_id", '')
    if not project_id:
        raise Http404("ID du projet manquant.")

    if action == 'main':
        url = direction + "/home/partials/content.html"

    if action == 'add':
        # Chercher le projet correspondant
        for project in all_projects:
            if str(project['id']) == project_id:
                selected_projects.append(project)
                request.session["selected_projects"] = selected_projects
                
    if action == 'remove':
        for project in all_projects:
            if str(project['id']) == project_id:
                selected_projects.remove(project)
                request.session["selected_project"] = selected_projects
                return redirect('main')

    # Vérifier si le projet est déjà sélectionné
    # deja_ajoute = False
    # for p in selected_projects:
    #    if str(p['id']) == project_id:
    #        deja_ajoute = True
    #       break

    # Ajouter le projet s'il n'est pas encore sélectionné
    # if not deja_ajoute:
    #    selected_projects.append(project)
    #    request.session["selected_projects"] = selected_projects
    #    request.session.modified = True  # Pour bien sauvegarder les changements

    # Retourner le contenu partiel du modal avec les projets sélectionnés
    return render(request, url, {"selected_projects": selected_projects})

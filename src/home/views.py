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

    # Vérifie si 'selected_projects' existe dans la session, sinon créer la clé avec une liste vide
    if "selected_projects" not in request.session:
        request.session["selected_projects"] = []

    # Récupérer les projets sélectionnés dans la session
    selected_projects = request.session["selected_projects"]

    # Récupérer l'ID du projet depuis la requête
    project_id = str(request.GET.get("project_id", '')).strip()
    if not project_id:
        raise Http404("ID du projet manquant.")

    if action == 'add':
        # Chercher le projet correspondant
        project = next((p for p in all_projects if str(p['id']) == project_id), None)
        if not project:
            raise Http404("Projet non trouvé.")

        # Ajouter le projet dans la liste des projets sélectionnés s'il n'est pas déjà dedans
        if not any(p['id'] == project_id for p in selected_projects):
            selected_projects.append(project)
            # Sauvegarder les projets sélectionnés dans la session
            request.session["selected_projects"] = selected_projects
            request.session.modified = True  # Important pour garantir la persistance des données

    # Retourner le contenu partiel du modal avec les projets sélectionnés
    return render(request, url, {"selected_projects": selected_projects})

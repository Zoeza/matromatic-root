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
    # Définir la langue par défaut si elle n'est pas déjà définie
    if not request.session.get('language'):
        request.session['language'] = 'en-us'

    # Initialiser les listes dans la session si elles n'existent pas
    if "selected_projects" not in request.session:
        request.session["selected_projects"] = []

    if "click_counts" not in request.session:
        request.session["click_counts"] = {}

    direction = request.session['language']
    url = direction + "/home/partials/content.html"

    # Charger les données depuis le fichier JSON
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            page_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise Http404("Erreur lors du chargement du fichier JSON.")

    all_projects = page_data.get('projects', {}).get('realizations', [])
    selected_projects = request.session["selected_projects"]
    click_counts = request.session["click_counts"]

    # Obtenir l'ID du projet depuis la requête
    project_id = request.GET.get("project_id", '')
    if not project_id:
        raise Http404("ID du projet manquant.")

    current_count = click_counts.get(project_id, 0)

    if action == 'add':
        deja_ajoute = False
        for project in selected_projects:
            if str(project['id']) == project_id:
                project['click_counts'] = project.get('click_counts', 0) + 1
                deja_ajoute = True
                break

        if not deja_ajoute:
            for project in all_projects:
                if str(project['id']) == project_id:
                    new_project = {
                        'id': project.get('id'),
                        'title': project.get('title'),
                        'description': project.get('description'),
                        'img': project.get('img'),
                        'click_counts': 1
                    }
                    selected_projects.append(new_project)

        # Sauvegarder les changements dans la session
        request.session["selected_projects"] = selected_projects
        request.session.modified = True

        context = {
            'selected_projects': selected_projects,
            'click_counts': click_counts,
        }
        return render(request, url, context)

    if action == 'remove':
        for project in selected_projects:
            if str(project['id']) == project_id:
                selected_projects.remove(project)
                break  # Sortir de la boucle après suppression

        request.session["selected_projects"] = selected_projects
        request.session.modified = True

        return render(request, url, {"selected_projects": selected_projects})

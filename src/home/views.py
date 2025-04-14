from django.shortcuts import render, redirect
import json
import os
from django.http import Http404
from django.views.decorators.http import require_POST


def home(request):
    if not request.session.get('language'):
        request.session['language'] = 'en-us'

    direction = request.session['language']
    url = direction + "/home/index.html"
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')

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


def increment_click(request):
    project_id = request.GET.get("project_id", '')
    if not project_id:
        raise Http404("ID du projet manquant.")

    # Incrémenter le compteur
    click_counts = request.session.get("click_counts", {})
    click_counts[project_id] = click_counts.get(project_id, 0) + 1
    request.session["click_counts"] = click_counts

    # Ajouter à la liste des projets sélectionnés
    selected_projects = request.session.get("selected_projects", [])
    if project_id not in selected_projects:
        selected_projects.append(project_id)
    request.session["selected_projects"] = selected_projects


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

    return redirect("/?show_modal=true")


def project_modal_content(request, action):
    direction = request.session.get('language', 'en')
    url = direction + "/home/index.html"
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            page_data = json.load(file)
    except FileNotFoundError:
        raise Http404("Fichier JSON introuvable.")
    except json.JSONDecodeError:
        raise Http404("Erreur de lecture JSON.")

    projects = page_data.get('projects', {}).get('realizations', [])

    if action == 'add':
        project_id = request.GET.get("project_id", '')
        if not project_id:
            raise Http404("ID du projet manquant.")

        for project in projects:
            if project_id == project['id']:
                request.session["selected_projects"] = project
                break
        else:
            raise Http404("Projet non trouvé.")

    elif action == 'remove':
        request.session.pop("selected_projects", None)

    return render(request, url, {"selected_projects": request.session.get("selected_projects", {})})

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

    # Compteurs de clics
    click_counts = request.session.get("click_counts", {})
    for project in page_data.get("projects", {}).get("realizations", []):
        project_id = str(project.get("id"))
        project["click_count"] = click_counts.get(project_id, 0)

    # Récupérer les projets sélectionnés
    selected_ids = request.session.get("selected_projects", [])
    selected_projects = [p for p in page_data["projects"]["realizations"] if str(p["id"]) in selected_ids]

    return render(request, url, {
        'data': page_data,
        'selected_projects': selected_projects
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

    return redirect("/?show_modal=true")


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
    direction = request.session['language']
    url = direction + "/home/partials/content.html"

    page_data = request.GET.get("page_data")

    if action == 'main':
        return render(request, url, {'page':page_data})

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
    direction = request.session['language']
    url = direction + "/home/partials/content.html"
    page_data = request.GET.get("page_data")
    if action == 'main':
        url = direction + "/home/index.html"

    if action == 'add':
        project_id = request.GET.get("project_id", '')
        if not project_id:
            raise Http404("ID du projet manquant.")

        selected_projects = request.session.get("selected_projects", [])

        # Chercher et ajouter le projet dans la session
        for p in page_data["projects"]["realizations"]:
            if str(p["id"]) == project_id:
                selected_projects.append(p)  # Ajouter toutes les infos du projet
                break  # Dès qu'on trouve le projet, on arrête la recherche

        # Sauvegarder la liste des projets sélectionnés dans la session
        request.session["selected_projects"] = selected_projects

    return render(request, url, {})

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

    if "selected_projects" not in request.session:
        request.session["selected_projects"] = page_data.get('projects', {}).get('realizations', {})

    return render(request, url, {
        'data': page_data,
    })


def project_modal_content(request, action):
    if not request.session.get('language'):
        request.session['language'] = 'en-us'

    if "selected_projects" not in request.session:
        request.session["selected_projects"] = []

    direction = request.session['language']
    url = direction + "/home/partials/content.html"

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'page.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            page_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise Http404("Erreur lors du chargement du fichier JSON.")

    all_projects = page_data.get('projects', {}).get('realizations', [])
    selected_projects = request.session["selected_projects"]
    project_id = request.GET.get("project_id", '')

    if not project_id:
        raise Http404("ID du projet manquant.")

    if action == 'add':
        deja_ajoute = False
        for project in selected_projects:
            if str(project['id']) == project_id:
                project['click_counts'] = project.get('click_counts', 0) + 1
                deja_ajoute = True

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
        }
        return render(request, url, context)

    if action == 'decrement':
        for project in selected_projects:
            if str(project['id']) == project_id:
                if project['click_counts'] > 1:
                    project['click_counts'] = project.get('click_counts', 0) - 1
                else:
                    selected_projects.remove(project)
        request.session["selected_projects"] = selected_projects
        request.session.modified = True
        return render(request, url, {"selected_projects": selected_projects})

    if action == 'remove':
        for project in selected_projects:
            if str(project['id']) == project_id:
                selected_projects.remove(project)

        request.session["selected_projects"] = selected_projects
        request.session.modified = True

        return render(request, url, {"selected_projects": selected_projects})

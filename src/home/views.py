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

    if "projects_list" not in request.session:
        request.session["projects_list"] = page_data.get('projects', {}).get('realizations', {})

    return render(request, url, {
        'data': page_data,
        'projects_list': request.session.get("projects_list", {})
    })


def project_modal_content(request, action):
    if not request.session.get('language'):
        request.session['language'] = 'en-us'

    direction = request.session['language']
    url = direction + "/home/partials/content.html"

    all_projects = request.session.get("projects_list", {})
    selected_projects = request.session["selected_projects"]
    project_id = request.GET.get("project_id", '')

    if action == 'add':
        if project_id not in selected_projects:
            selected_projects[project_id] = all_projects[project_id]
            all_projects[project_id]['click_counts'] = 1
        else:
            all_projects[project_id]['click_counts'] += 1

    if action == 'decrement':
        if project_id in selected_projects:
            if selected_projects[project_id].get('click_counts', 0):
                selected_projects[project_id]['click_counts'] -= 1
            else:
                del selected_projects[project_id]

    if action == 'remove':
        if project_id in selected_projects:
            del selected_projects[project_id]

    context = {
        'selected_projects': selected_projects,
    }
    return render(request, url, context)

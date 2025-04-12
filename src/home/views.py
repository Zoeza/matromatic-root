from django.shortcuts import render, redirect
import json
import os
from django.http import Http404
from django.views.decorators.http import require_POST


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

    click_counts = request.session.get("click_counts", {})
    for project in page_data.get("projects", {}).get("realizations", []):
        project_id = str(project.get("id"))
        project["click_count"] = click_counts.get(project_id, 0)

    # On récupère l’ID du projet cliqué depuis l’URL
    open_modal_id = request.GET.get("project_id")

    context = {
        'data': page_data,
        'open_modal_id': open_modal_id,
    }

    return render(request, url, context)


@require_POST
def increment_click(request):
    project_id = request.POST.get("project_id")
    if not project_id:
        raise Http404("ID du projet manquant.")

    click_counts = request.session.get("click_counts", {})
    click_counts[project_id] = click_counts.get(project_id, 0) + 1
    request.session["click_counts"] = click_counts

    # On redirige vers la page d'accueil avec l’ID du projet cliqué
    return redirect(f"{request.path_info}?project_id={project_id}")

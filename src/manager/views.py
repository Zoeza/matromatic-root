from django.shortcuts import render, redirect
from .forms import TopPageForm


def dashboard(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/manager/dashboard.html"

    return render(request, url, {})


def home_manager(request, action):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    nav_side = 'home'
    # -- main page show -- #
    if action == "main":
        url = direction + "/manager/home-manager.html"
        tab = request.session.get('tab')
        request.session['tab'] = None
        context = {
            'nav_side': nav_side,
            'tab': tab,
        }
        return render(request, url, context)
    # ---------------------- top page----------------------
    if action == 'create_top_page':
        if request.method == 'POST':
            top_page_form = TopPageForm(request.POST, request.FILES)
            top_page_form.save()
        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'main')

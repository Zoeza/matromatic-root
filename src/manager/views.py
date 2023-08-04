from django.shortcuts import render, redirect
from .forms import TopPageForm
from home.models import TopPage


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

        top_pages = TopPage.objects.all()
        context = {
            'nav_side': nav_side,
            'tab': tab,
            'top_pages': top_pages,
        }
        return render(request, url, context)
    # ---------------------- create top page---------------------- #
    if action == 'create_top_page':
        if request.method == 'POST':
            TopPage(language=request.POST.get('language', False),
                    head_title=request.POST.get('head_title', False),
                    head_text=request.POST.get('head_text', False),
                    company_name=request.POST.get('company_name', False),
                    company_slogan=request.POST.get('company_slogan', False),
                    logo_main=request.FILES.get('logo_main'),
                    logo_head=request.FILES.get('logo_head'),
                    iphone_image=request.FILES.get('iphone_image'),
                    macbook_image=request.FILES.get('macbook_image'),
                    ipad_image= request.FILES.get('ipad_image'), ).save()
        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'main')
    # ---------------------- edit top page---------------------- #
    if action == 'edit_top_page':
        pass





from django.shortcuts import render, redirect
from home.models import TopPage, Content, Service, OurProcess, Performance, Client, Partner, Project, Footer
from .forms import TopPageForm, ContentForm, FooterForm, ServiceForm, ProcessForm, ClientForm, PartnerForm, \
    ProjectForm, PerformanceForm


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
    if action == "top_page":
        url = direction + "/manager/home-manager.html"
        tab = request.session.get('tab')
        request.session['tab'] = None

        footers = Footer.objects.all()
        top_pages = TopPage.objects.all()
        main_contents = Content.objects.all()
        services_form = ServiceForm()
        services = Service.objects.all()
        process_steps = OurProcess.objects.all()
        performances = Performance.objects.all()
        clients = Client.objects.all()
        partners = Partner.objects.all()
        projects = Project.objects.all()

        context = {
            'nav_side': nav_side,
            'tab': tab,
            'top_pages': top_pages,
            'main_contents': main_contents,
            'services_form': services_form,
            'services': services,
            'process_steps': process_steps,
            'performances': performances,
            'clients': clients,
            'partners': partners,
            'projects': projects,
            'footers': footers,
        }
        return render(request, url, context)
    # ---------------------- create top page -------------------- #
    if action == 'create_top_page':
        if request.method == 'POST':
            top_page_form = TopPageForm(request.POST, request.FILES)
            if top_page_form.is_valid():
                top_page_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # -------------------- end create top page ------------------ #

    # ---------------------- edit top page ---------------------- #
    if action == 'edit_top_page':
        if request.method == 'POST':
            top_page_id = request.POST.get('top_page_id', False)
            selected_top_page = TopPage.objects.all().get(id=top_page_id)
            top_page_form = TopPageForm(request.POST, request.FILES, instance=selected_top_page)
            top_page_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
        # ------------------- end edit top page ---------------- #

        # -------------------- delete top page ----------------- #
        if action == 'delete_top_page':
            if request.method == 'POST':
                top_page_id = request.POST.get('top_page_id', False)
                selected_top_page = TopPage.objects.all().get(id=top_page_id)
                selected_top_page.delete()
                request.session['tab'] = 'top-page'
                return redirect('home-manager', 'top-page')
    # ----------------- end delete top page ---------------------- #

    # ---------------------- create main content -------------------- #
    if action == 'create_main_content':
        if request.method == 'POST':
            main_content_form = ContentForm(request.POST, request.FILES)
            if main_content_form.is_valid():
                main_content_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # -------------------- end create main content ------------------ #

    # -------------------- edit main content ------------------------- #
    if action == 'edit_main_content':
        if request.method == 'POST':
            main_content_id = request.POST.get('main_content_id', False)
            selected_main_content = Content.objects.all().get(id=main_content_id)
            main_content_form = ContentForm(request.POST, request.FILES, instance=selected_main_content)
            main_content_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end edit main content ---------------------- #

    # -------------------- delete main content ----------------------- #
    if action == 'delete_main_content':
        if request.method == 'POST':
            main_content_id = request.POST.get('main_content_id', False)
            selected_main_content = Content.objects.all().get(id=main_content_id)
            selected_main_content.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top-page')
    # ------------------- end delete main content -------------------- #

    # ---------------------- create new footer -------------------- #
    if action == 'create_new_footer':
        if request.method == 'POST':
            footer_form = FooterForm(request.POST, request.FILES)
            if footer_form.is_valid():
                footer_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # -------------------- end create footer ------------------ #

    # -------------------- edit new footer ------------------------- #
    if action == 'edit_footer':
        if request.method == 'POST':
            footer_id = request.POST.get('footer_id', False)
            selected_footer = Footer.objects.all().get(id=footer_id)
            footer_form = FooterForm(request.POST, instance=selected_footer)
            footer_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end edit footer ---------------------- #

    # -------------------- delete footer ----------------------- #
    if action == 'delete_main_content':
        if request.method == 'POST':
            footer_id = request.POST.get('footer_id', False)
            selected_footer = Footer.objects.all().get(id=footer_id)
            selected_footer.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end delete footer -------------------- #

    # ---------------------- add service ------------------------ #
    if action == 'add_new_service':
        if request.method == 'POST':
            service_form = ServiceForm(request.POST, request.FILES)
            if service_form.is_valid():
                service_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # ----------------- end  add service ------------------------ #

    # -------------------- edit service ------------------------- #
    if action == 'edit_service':
        if request.method == 'POST':
            service_id = request.POST.get('service_id', False)
            selected_service = Service.objects.all().get(id=service_id)
            service_form = ServiceForm(request.POST, request.FILES, instance=selected_service)
            service_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end edit service ---------------------- #

    # -------------------- delete service ----------------------- #
    if action == 'delete_service':
        if request.method == 'POST':
            service_id = request.POST.get('service_id', False)
            selected_service = Service.objects.all().get(id=service_id)
            selected_service.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end delete service -------------------- #

    # ------------------- add process step ---------------------- #
    if action == 'add_process_step':
        if request.method == 'POST':
            process_form = ProcessForm(request.POST, request.FILES)
            if process_form.is_valid():
                process_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top-page')
    # ---------------- end add process step---------------------- #

    # -------------------- edit process step--------------------- #
    if action == 'edit_process_step':
        if request.method == 'POST':
            process_step_id = request.POST.get('{process_step_id', False)
            selected_process_step = OurProcess.objects.all().get(id=process_step_id)
            process_form = ProcessForm(request.POST, request.FILES, instance=selected_process_step)
            process_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top-page')
    # ------------------- end edit process step------------------ #

    # -------------------- delete process step------------------- #
    if action == 'delete_process_step':
        if request.method == 'POST':
            process_step_id = request.POST.get('process_step_id', False)
            selected_process_step = OurProcess.objects.all().get(id=process_step_id)
            selected_process_step.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end delete process step---------------- #

    # ---------------------- add performance--------------------- #
    if action == 'add_performance':
        if request.method == 'POST':
            performance_form = PerformanceForm(request.POST)
            if performance_form.is_valid():
                performance_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # ---------------------- end add performance----------------- #

    # ------------------- edit performance ---------------------- #
    if action == 'edit_performance':
        if request.method == 'POST':
            performance_id = request.POST.get('performance_id', False)
            selected_performance = Performance.objects.all().get(id=performance_id)
            performance_form = PerformanceForm(request.POST, instance=selected_performance)
            performance_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------ end edit performance ------------------- #

    # ------------------- delete performance -------------------- #
    if action == 'delete_performance':
        if request.method == 'POST':
            performance_id = request.POST.get('performance_id', False)
            selected_performance = Performance.objects.all().get(id=performance_id)
            selected_performance.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------ end delete performance ----------------- #

    # ---------------------- add new client---------------------- #
    if action == 'add_new_client':
        if request.method == 'POST':
            client_form = ClientForm(request.POST, request.FILES)
            if client_form.is_valid():
                client_form.save()

        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # ---------------------- end add new client ----------------- #

    # -------------------- edit client -------------------------- #
    if action == 'edit_client':
        if request.method == 'POST':
            client_id = request.POST.get('client_id', False)
            selected_client = Client.objects.all().get(id=client_id)
            client_form = ClientForm(request.POST, request.FILES, instance=selected_client)
            client_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end edit client ----------------------- #

    # -------------------- delete client ------------------------ #
    if action == 'delete_client':
        if request.method == 'POST':
            client_id = request.POST.get('client_id', False)
            selected_client = Client.objects.all().get(id=client_id)
            selected_client.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end delete client --------------------- #

    # ---------------------- add new partner--------------------- #
    if action == 'add_new_partner':
        if request.method == 'POST':
            partner_form = PartnerForm(request.POST, request.FILES)
            if partner_form.is_valid():
                partner_form.save()
        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # ---------------------- end add new partner----------------- #

    # -------------------- edit partner ------------------------- #
    if action == 'edit_partner':
        if request.method == 'POST':
            partner_id = request.POST.get('partner_id', False)
            selected_partner = Partner.objects.all().get(id=partner_id)
            partner_form = PartnerForm(request.POST, request.FILES, instance=selected_partner)
            partner_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end edit partner----------------------- #

    # -------------------- delete partner ----------------------- #
    if action == 'delete_partner':
        if request.method == 'POST':
            partner_id = request.POST.get('partner_id', False)
            selected_partner = Partner.objects.all().get(id=partner_id)
            selected_partner.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end delete partner--------------------- #

    # ---------------------- add new  project-------------------- #
    if action == 'add_new_project':
        if request.method == 'POST':
            project_form = ProjectForm(request.POST, request.FILES)
            if project_form.is_valid():
                project_form.save()
        request.session['tab'] = 'top-page'
        return redirect('home-manager', 'top_page')
    # ---------------------- end add new  project---------------- #

    # -------------------- edit project ------------------------- #
    if action == 'edit_project':
        if request.method == 'POST':
            project_id = request.POST.get('project_id', False)
            selected_project = Project.objects.all().get(id=project_id)
            project_form = ProjectForm(request.POST, request.FILES, instance=selected_project)
            project_form.save()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end edit project----------------------- #

    # -------------------- delete project ----------------------- #
    if action == 'delete_project':
        if request.method == 'POST':
            project_id = request.POST.get('project_id', False)
            selected_project = Project.objects.all().get(id=project_id)
            selected_project.delete()
            request.session['tab'] = 'top-page'
            return redirect('home-manager', 'top_page')
    # ------------------- end delete project--------------------- #

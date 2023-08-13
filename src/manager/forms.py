from django.forms import ModelForm
from home.models import TopPage, Service, OurProcess, Performance, Partner, Client, Project, Content, Footer


class TopPageForm(ModelForm):
    class Meta:
        model = TopPage
        fields = "__all__"


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = "__all__"


class FooterForm(ModelForm):
    class Meta:
        model = Footer
        fields = "__all__"


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class ProcessForm(ModelForm):
    class Meta:
        model = OurProcess
        fields = "__all__"


class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = "__all__"


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = "__all__"


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

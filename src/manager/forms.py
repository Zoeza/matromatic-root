from django.forms import ModelForm
from .models import Home, MainContent, Footer, ContactUs, Service, OurProcess, SocialMedia, Client, Project


class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = "__all__"


class MainContentForm(ModelForm):
    class Meta:
        model = MainContent
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


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"


class SocialMediaForm(ModelForm):
    class Meta:
        model = SocialMedia
        fields = "__all__"

from django.forms import ModelForm
from django import forms
from .models import TopPage


class TopPageForm(ModelForm):
    language = forms.CharField(required=True)
    head_title = forms.CharField(required=True)
    head_text = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    company_slogan = forms.CharField(required=True)
    logo_main = forms.FileField(required=True)
    logo_head = forms.FileField(required=True)
    iphone_image = forms.FileField(required=True)
    macbook_image = forms.FileField(required=True)
    ipad_image = forms.FileField(required=True)

    class Meta:
        model = TopPage
        fields = ('language', 'head_title', 'head_text', 'company_name', 'company_slogan', 'logo_main', 'logo_head',
                  'iphone_image', 'macbook_image', 'ipad_image')

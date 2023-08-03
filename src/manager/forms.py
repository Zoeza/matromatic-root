from django.forms import ModelForm
from django import forms
from .models import TopPage


class TopPageForm(ModelForm):
    class Meta:
        model = TopPage
        fields = ('language', 'head_title', 'head_text', 'company_name', 'company_slogan', 'logo_main', 'logo_head',
                  'iphone_image', 'macbook_image', 'ipad_image')
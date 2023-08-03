from django.db import models


class HeaderPage(models.Model):
    language = models.CharField(max_length=50, blank=True)
    head_title = models.CharField(max_length=50, blank=True)
    head_text = models.CharField(max_length=80, blank=True)
    company_name = models.CharField(max_length=80, unique=True)
    company_slogan = models.CharField(max_length=80, blank=True)
    logo_main = models.FileField(upload_to='logo_main/', null=True)
    logo_head = models.FileField(upload_to='logo_head/', null=True)
    iphone_image = models.FileField(upload_to='iphone_image/', null=True)
    macbook_image = models.FileField(upload_to='macbook_image/', null=True)
    ipad_image = models.FileField(upload_to='ipad_image/', null=True)

    class Meta:
        verbose_name = "top page"

    def __str__(self):
        return self.language

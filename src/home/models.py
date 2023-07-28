from django.db import models


class Header(models.Model):
    sku = models.CharField(max_length=50, blank=True)
    head_title = models.CharField(max_length=50, blank=True)
    head_text = models.CharField(max_length=80, blank=True)
    company_name = models.CharField(max_length=80, unique=True)
    company_slogan = models.CharField(max_length=80, blank=True)
    company_description = models.TextField(max_length=200, blank=True)
    logo_main = models.FileField(upload_to='logo_main/', null=True)
    logo_head = models.FileField(upload_to='logo_head/', null=True)

    def __str__(self):
        return self.sku


class SocialMedia(models.Model):
    name = models.CharField(max_length=70, blank=True)
    link = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name


class BackgroundImg(models.Model):
    name = models.CharField(max_length=70, blank=True)
    img = models.ImageField(upload_to='background_img', null=True, blank=True)

    def __str__(self):
        return self.name

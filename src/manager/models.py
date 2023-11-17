from django.db import models


# ------------------------------ Home ------------------------------- #

class Home(models.Model):
    language = models.CharField(max_length=50, blank=True)
    head_title = models.CharField(max_length=50, blank=True)
    head_text = models.CharField(max_length=80, blank=True)
    company_name = models.CharField(max_length=80, unique=True)
    company_slogan = models.CharField(max_length=80, blank=True)
    logo_main = models.FileField(upload_to='logo_main/', null=True)
    logo_head = models.FileField(upload_to='logo_head/', null=True)

    class Meta:
        verbose_name = "home"

    def __str__(self):
        return self.language


# ------------------------------ About us ------------------------------- #
class About_us(models.Model):
    language = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=150, blank=True)
    company_description = models.TextField(max_length=500, blank=True)
    about_us_photo = models.ImageField(upload_to='about_us/about_us_photo', blank=True)

    class Meta:
        verbose_name = "about_us"

    def __str__(self):
        return self.language


# ------------------------------ Service ------------------------------- #
class Service(models.Model):
    language = models.CharField(max_length=50, blank=True)
    service_title = models.CharField(max_length=70, blank=True)
    service_description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='service/', blank=True)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.service_title


# ------------------------------ Processes ------------------------------- #

class OurProcess(models.Model):
    language = models.CharField(max_length=50, blank=True)
    process_number = models.IntegerField(blank=True)
    process_title = models.CharField(max_length=100, blank=True)
    process_description = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name = "process"

    def __str__(self):
        return self.process_title

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
class MainContent(models.Model):
    language = models.CharField(max_length=50, blank=True)
    about_us_title = models.CharField(max_length=150, blank=True)
    about_us_description = models.TextField(max_length=500, blank=True)
    about_us_photo = models.ImageField(upload_to='about_us/about_us_photo', blank=True)
    our_process_title = models.CharField(max_length=150, blank=True)
    our_process_description = models.TextField(max_length=500, blank=True)
    our_service_title = models.CharField(max_length=150, blank=True)
    our_service_description = models.TextField(max_length=500, blank=True)
    contact_title = models.CharField(max_length=150, blank=True)
    contact_description = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "main content"

    def __str__(self):
        return self.language


# ------------------------------ Service ------------------------------- #
class Service(models.Model):
    service_title = models.CharField(max_length=70, blank=True)
    service_description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='service/', blank=True)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.service_title


# ------------------------------ Processes ------------------------------- #
class OurProcess(models.Model):
    process_number = models.IntegerField(blank=True)
    process_title = models.CharField(max_length=100, blank=True)
    process_description = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name = "process"

    def __str__(self):
        return self.process_title


# ------------------------------ Projects ----------------------------- #
class Project(models.Model):
    project_type = models.CharField(max_length=100, unique=True)
    project_name = models.CharField(max_length=50, unique=True)
    project_photo = models.ImageField(upload_to='projects/project_photo', null=True, blank=True)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name


# ------------------------------ Clients ----------------------------- #
class Client(models.Model):
    client_name = models.CharField(max_length=50, unique=True)
    client_logo = models.ImageField(upload_to='clients/client_logo', null=True, blank=True)
    client_website = models.URLField(max_length=250)

    class Meta:
        verbose_name = "client"

    def __str__(self):
        return self.client_name


# ------------------------------ Contact us ----------------------------- #
class ContactUs(models.Model):
    language = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300)
    phone = PhoneNumberField(blank=True, help_text='Contact phone number')
    mobile = PhoneNumberField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "contact"

    def __str__(self):
        return self.language


# ------------------------------ Social Media ------------------------- #
class SocialMedia(models.Model):
    name = models.CharField(max_length=70, blank=True)
    link = models.URLField(max_length=250)
    icon = models.CharField(max_length=70, blank=True)

    class Meta:
        verbose_name = "social media"

    def __str__(self):
        return self.name


# ------------------------------ Footer -------------------------------- #

class Footer(models.Model):
    language = models.CharField(max_length=50, blank=True)
    made_by = models.CharField(max_length=80, blank=True)
    link = models.URLField(max_length=250)

    class Meta:
        verbose_name = "footer"

    def __str__(self):
        return self.language

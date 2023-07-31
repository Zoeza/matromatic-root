from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class TopPage(models.Model):
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


class Content(models.Model):
    sku = models.CharField(max_length=50, blank=True)
    why_us_raison1 = models.TextField(max_length=300, blank=True)
    why_us_raison2 = models.TextField(max_length=300, blank=True)
    why_us_photo = models.ImageField(upload_to='content/why_us_photo', blank=True)
    why_us_video_src = models.CharField(max_length=50, blank=True)

    our_process_intro = models.TextField(max_length=200, blank=True)
    partners_intro = models.TextField(max_length=200, blank=True)
    projects_intro = models.TextField(max_length=200, blank=True)
    client_count = models.CharField(max_length=50, blank=True)
    main_background_image = models.ImageField(upload_to='content/main_background_image', blank=True)

    performance_intro = models.TextField(max_length=200, blank=True)
    performance_record_description = models.TextField(max_length=200, blank=True)
    performance_record_breaking = models.DecimalField(max_digits=3, decimal_places=0, default=0,
                                                      validators=PERCENTAGE_VALIDATOR)

    service = models.ForeignKey(
        'home.Performance', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "content"

    def __str__(self):
        return self.sku


class Footer(models.Model):
    sku = models.CharField(max_length=50, blank=True)
    copyright = models.CharField(max_length=80, blank=True)
    made_by = models.CharField(max_length=80, blank=True)
    made_by_link = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "footer"

    def __str__(self):
        return self.sku


class Service(models.Model):
    service_title = models.CharField(max_length=70, blank=True)
    service_description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='service/', blank=True)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.service_title


class OurProcess(models.Model):
    process_number = models.IntegerField(blank=True)
    process_title = models.CharField(max_length=70, blank=True)
    process_description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='our_process/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "processe"

    def __str__(self):
        return self.process_title


class Partner(models.Model):
    partner_name = models.CharField(max_length=50, unique=True)
    partner_logo = models.ImageField(upload_to='partner/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "partner"

    def __str__(self):
        return self.partner_name


class Client(models.Model):
    client_name = models.CharField(max_length=50, unique=True)
    client_logo = models.ImageField(upload_to='clients/client_logo', null=True, blank=True)
    client_comment = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name = "client"

    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_name = models.CharField(max_length=50, unique=True)
    project_photo = models.ImageField(upload_to='projects/project_photo', null=True, blank=True)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name


class SocialMedia(models.Model):
    name = models.CharField(max_length=70, blank=True)
    link = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=70, blank=True)

    class Meta:
        verbose_name = "social media"

    def __str__(self):
        return self.name


class Performance(models.Model):
    domain = models.CharField(max_length=100, blank=True)
    percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0,
                                     validators=PERCENTAGE_VALIDATOR)

    class Meta:
        verbose_name = "performance"

    def __str__(self):
        return self.domain


class TopBackgroundImage(models.Model):
    name = models.CharField(max_length=70, blank=True)
    img = models.ImageField(upload_to='top_background_img/', null=True, blank=True)

    class Meta:
        verbose_name = "top background image"

    def __str__(self):
        return self.name

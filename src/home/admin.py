from django.contrib import admin
from .models import TopPage, Content, Footer, Service, OurProcess, Partner, SocialMedia, Client, \
    Project, Performance

# Register your models here.
admin.site.register(TopPage)
admin.site.register(Content)
admin.site.register(Footer)

admin.site.register(Service)
admin.site.register(OurProcess)
admin.site.register(Partner)
admin.site.register(Client)
admin.site.register(Performance)
admin.site.register(Project)

admin.site.register(SocialMedia)

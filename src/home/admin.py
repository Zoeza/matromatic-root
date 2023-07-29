from django.contrib import admin
from .models import Header,  Main,Footer, Service, OurProcess, Partner, SocialMedia, BackgroundImage, Client

# Register your models here.
admin.site.register(Header)
admin.site.register(Main)
admin.site.register(Footer)

admin.site.register(Service)
admin.site.register(OurProcess)
admin.site.register(Partner)
admin.site.register(Client)

admin.site.register(SocialMedia)
admin.site.register(BackgroundImage)

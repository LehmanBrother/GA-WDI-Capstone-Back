from django.contrib import admin
from .models import Agency, Federal_Account, Consumer_Reference, Agency_Raw, Federal_Account_Raw

# Register your models here.
admin.site.register(Agency)
admin.site.register(Federal_Account)
admin.site.register(Consumer_Reference)
admin.site.register(Agency_Raw)
admin.site.register(Federal_Account_Raw)
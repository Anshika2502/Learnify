from django.contrib import admin
from .models import Student , Pricing , Subscription

# Register your models here.
admin.site.register(Student)
admin.site.register(Pricing)
admin.site.register(Subscription)
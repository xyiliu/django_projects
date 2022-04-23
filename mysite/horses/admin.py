from django.contrib import admin

# Register your models here.
from horses.models import Breed, Horse

# Register your models here.

admin.site.register(Breed)
admin.site.register(Horse)

from django.contrib import admin
from . models import Rev


class RevAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'review', 'genre', 'age')


admin.site.register(Rev, RevAdmin)  # need to register with admin site to be visible

# python manage.py createsuperuser

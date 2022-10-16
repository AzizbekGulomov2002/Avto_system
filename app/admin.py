from django.contrib import admin

# Register your models here.
from .models import Avtomobil
class Avto_Admin(admin.ModelAdmin):
    list_display = ['nomi','yil','manzil','probeg','narx']
    list_per_page = 10
    ordering = ('nomi','yil','manzil','probeg','narx')
    search_fields = ['nomi','yil','manzil','probeg','narx']
admin.site.register(Avtomobil, Avto_Admin)



# admin.site.register(Avtomobil)


from .models import Category
admin.site.register(Category)

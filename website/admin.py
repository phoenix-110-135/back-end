from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')
    empty_value_display = '-none-'

admin.site.register(Contact,ContactAdmin)
# Register your models here.

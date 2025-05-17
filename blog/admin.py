from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-none-'
    list_display = ('title','author','counted_view','status','published_date','created_date')
    list_filter = ('status','author')
    # ordering = ['-created_date']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)

# Register your models here.

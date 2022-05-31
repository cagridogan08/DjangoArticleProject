from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title','author','created_date')
    list_display_links=('title','created_date')
    search_fields=["title"]

    list_filter=["created_date"]
    class Meta:
        model = Article
    
    


admin.site.register(Article,ArticleAdmin)
from django.contrib import admin
#from .models import MyUser

from .models import Article, Publication

class PublicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publication, PublicationAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)

#admin.site.register(MyUser)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import Article, Publication

class PublicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publication, PublicationAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)

admin.site.register(User, UserAdmin)
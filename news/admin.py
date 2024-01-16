
from .models import Author, Post, PostCategory, Comment, Appointment, Category, MyModel
from django.contrib import admin
from modeltranslation.admin import \
    TranslationAdmin

admin.site.register(Category, TranslationAdmin)
admin.site.register(Author)
admin.site.register(Post, TranslationAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Appointment)
admin.site.register(MyModel)

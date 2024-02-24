from django.contrib import admin
from .models import Category , Subscribtion , Blog, Rate

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title" , "category")
    prepopulated_fields = {"slug" : ("title" ,)}#slug

admin.site.register(Category)
admin.site.register(Subscribtion)
admin.site.register(Blog , BlogAdmin)
admin.site.register(Rate)


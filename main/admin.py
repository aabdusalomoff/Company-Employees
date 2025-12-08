from django.contrib import admin

from .models import Author,Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name','is_active')

admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    list_filter = ('created_at','is_active') 

admin.site.register(Book,BookAdmin)


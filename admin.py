from django.contrib import admin
from myproject.myapp.models import author
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site register(Author,AuthorAdmin)

# Register your models here.

from django.contrib import admin
from .models import Farmers, Blogs, Products, Commenters, Aboutus, Features, Banner, Contact, Newsletter

# Register your models here.
admin.site.register(Farmers)
admin.site.register(Blogs)
admin.site.register(Commenters)
admin.site.register(Aboutus)
admin.site.register(Features)
admin.site.register(Banner)
admin.site.register(Contact)
admin.site.register(Newsletter)
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}












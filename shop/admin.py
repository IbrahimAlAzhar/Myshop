from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug'] # display on the admin
    prepopulated_fields = {'slug': ('name',)} # when you add the name then the slug is created automatically,this one is called prepopulated fields


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available','created','updated'] # this attributes shows in admin page
    list_filter = ['available', 'created','updated','category'] # this attributes use for filtering
    list_editable = ['price','stock','available'] # only these attributes can only edit by admin,list editable must be in list_display
    prepopulated_fields = {'slug': ('name',)} # specified fields where value is automatically save


admin.site.register(Product, ProductAdmin)


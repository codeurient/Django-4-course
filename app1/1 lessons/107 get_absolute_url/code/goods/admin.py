from django.contrib import admin
from goods.models import Categories, Products



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }    
    list_display = ['name', ]




@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = ['name', 'quantity', 'price', 'discount']

    list_editable = ['discount']

    search_fields = ['name']

    list_filter = ['discount', 'quantity', 'category']


    fields = [
            'name', 
            'category', 
            'slug', 
            'description', 
            'image', 
            ('price', 'discount'),
            'quantity', 
        ]
    

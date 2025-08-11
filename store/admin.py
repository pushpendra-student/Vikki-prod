from django.contrib import admin
from . import models


admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    
    def products_count(self,collection):
        return collection.products_count
    

        
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10    


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at', 'customer']
    list_select_related = ['customer']
    list_per_page = 10
    







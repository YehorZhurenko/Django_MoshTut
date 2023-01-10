from django.contrib import admin
from . import models
from django.utils.html import format_html, urlencode
from django.db.models import Count
from django.urls import reverse



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    
    @admin.display(ordering='products_count')
    def products_count(self, collection): #ins column with products count into collection table
        url = (reverse('admin:store_product_changelist') #app-model_page format
            +'?'
            + urlencode({'collection_id': str(collection.id)}))
            
        return format_html('<a href = "{}">{}</a>', url, collection.products_count)#redirect to the from collection to roducts table  
        #return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))
        


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['title', 'unit_price', 'inventory_status', 'collection_title'] #список отображаемых полей
    list_editable = ['unit_price'] #    разрешение редактирования в админ-панели
    list_filter = ['collection', 'last_update']
    list_per_page = 10  #количество строк на странице
    list_select_related = ['collection']

    def collection_title(self,product): # Метод для возврата названия коллекции 
        return product.collection.title


    @admin.display(ordering= 'inventory')
    def inventory_status(self,product):
        if product.inventory < 10:  
            return 'Low'
        return 'OK'



@admin.register(models.Order)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['id', 'placed_at', 'customer'] #список отображаемых полей
    list_per_page = 10  #количество строк на странице
    list_select_related = ['customer']

    def collection_title(self,order): # Метод для возврата названия коллекции 
        return order.collection.title



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =  ['first_name', 'last_name', 'membership'] #список отображаемых полей
    list_editable = ['membership'] #    разрешение редактирования в админ-панели
    list_per_page = 10  #количество строк на странице
    ordering = ['first_name', 'last_name'] #Сортировка
    search_fields = ['first_name__istartswith', 'last_name__istartswith'] #fname and sname searchfield 




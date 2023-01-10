from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, OrderItem, Customer, Collection
from django.db.models import Q,F, ExpressionWrapper, Value


def say_hello(request):
    
   
    queryset = Product.objects.filter(

        Q(inventory__lt=10) | Q(unit_price__lt=20)  

    )
    
        #queryset = Product.objects.filter(inventory = F('unit_price'))

    #queryset= Product.objects.order_by('unit_price', '-title') 

    #queryset = Product.objects.values('id', 'title', 'orderitem__product_id').order_by('title').distinct()

    #queryset = Product.objects.all()[0:10]
    '''
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField())

    queryset = Product.objects.annotate(discounted_price=discounted_price)
    '''

    """     collection = Collection()
    collection.title = ('GamesWOW') 
    collection.featured_product = Product(pk = 2)
    collection.save()    """ 

    Collection.objects.filter(pk=11).update(featured_product = None) #update
    Collection.objects.filter(pk=5).update(featured_product = "3")     #update


    collection = Collection() #adding new line
    collection.title = ("COreWraft")
    collection.featured_product = Product(pk = 5)
    collection.save() # saving it    

    collection = Collection()
    collection.title = ("MukeDukem") 
    collection.featured_product = Product(pk = 3)
    collection.save() 
     
    collection = Collection()
    collection.title = ("FTL")
    collection.featured_product = Product(pk = 2)
    collection.save()

    Collection.objects.filter(pk = 4).update(title = "newTitle",)
    collection = Collection(pk=5)
    #collection.delete() #удаление оного элемента

    #Collection.objects.filter(id__gt = 5).delete() #удаление нескльких элементов

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
    
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.db.models.aggregates import Count

# Create your views here.
def  hello(request):
    try:
        q = Product.objects.all()
        list(q)
        queryset = q.filter(sku='12')
    except:
        return HttpResponse("Product not found")
    return render(request, 'hello.html', {'name': 'nitin', 'product': queryset})
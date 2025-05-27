from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def  hello(request):
    try:
        queryset = Product.objects.filter(title='umbrella')
    except:
        return HttpResponse("Product not found")
    return render(request, 'hello.html', {'name': 'nitin', 'product': queryset})
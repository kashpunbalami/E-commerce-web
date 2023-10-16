from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from chiya_app.models import product
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def chiya_home(request):
    return render(request, 'home.html')

def chiya_about(request):
    return render(request, 'about.html')

def chiya_contacts(request):
    return render(request, 'contacts.html')

def product_list(request):
    product_data=product.objects.all()
    data={
        'product_data':product_data
    }
    return render(request, "product.html", data)

def save_product(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        p=product(name=name,price=price,description=description)
        p.save()
        n='product added'
    return render(request, "add_product.html", {'n':n})
    #return HttpResponse("product added sucessfully")

def delete_chiya(request, product_id):
    Product=product.objects.get(pk=product_id)
    Product.delete()
    return HttpResponse('product is deleted')

    




from django.shortcuts import render,HttpResponse
from bakery_item_app.models import bakery
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def display_bakery(request):
    bakery_data=bakery.objects.all()
    data={
        'bakery_data':bakery_data

    }
    return render(request, 'bakery_display.html', data)

def add_bakery(request):
    n=''
    if request.method=="POST":
        name=request.POST.get("item")
        price=request.POST.get("price")
        description=request.POST.get("description")
        b=bakery(name=name, price=price, description=description)
        b.save()
        n="item added"
    return render(request, "add_bakery.html", {'n':n})

def delete_bakery(request, item_id):
    if item_id:
        try:
            my_object=bakery.objects.get(pk=item_id)
            my_object.delete()
            return HttpResponse("item removed")
        except:
            return HttpResponse("No valid item choosen")
    items = bakery.objects.all()
    context ={
        'items': items
    }
    return render(request, 'delete_bakery.html', context)



    

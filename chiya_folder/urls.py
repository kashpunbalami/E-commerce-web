"""
URL configuration for chiya_folder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chiya_app.views import chiya_home
from chiya_app.views import chiya_about
from chiya_app.views import chiya_contacts
from chiya_app.views import product_list
from chiya_app.views import save_product
from bakery_item_app.views import display_bakery
from bakery_item_app.views import add_bakery
from bakery_item_app.views import delete_bakery
from chiya_app.views import delete_chiya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chiya_home, name='chiya_home'),
    path('chiya_about/', chiya_about, name='chiya_about'),
    path('chiya_contacts/', chiya_contacts, name='chiya_contacts'),
    path('product_list/', product_list, name="product_list"),
    path('save_product/', save_product, name="save_product"),
    path('display_bakery/', display_bakery, name="display_bakery"),
    path('add_bakery/', add_bakery, name="add_bakery"),
    path('delete_bakery/', delete_bakery , name="delete_bakery"),
    path('delete_bakery/<item_id>/', delete_bakery , name="delete_bakery"),    
    path('delete_chiya/', delete_chiya , name="delete_chiya"),
    path('delete_chiya/<int:product_id>/', delete_chiya , name="delete_chiya"),
    
]

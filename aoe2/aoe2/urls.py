"""aoe2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from civs.views import civs_view
from pages.views import home_view, contact_view, aoe_view
from product.views import product_detail_view, product_create_view, redener_intial_data, product_lookup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('contact/', contact_view),
    path('aoe/', aoe_view),
    path('product/', product_detail_view),
    path('create/', redener_intial_data),
    path('lookup/<int:id>/', product_lookup),
    path('civs/', civs_view),
]

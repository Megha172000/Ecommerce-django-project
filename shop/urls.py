from django.urls import path
from .import views

urlpatterns = [
    path('',views.shopindex,name='shopindex'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('productview/',views.productView,name='productview'),
    path('checkout/',views.checkout,name='checkout'),



]
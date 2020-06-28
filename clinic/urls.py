from django.urls import path
from .views import cart, checkout, index


urlpatterns = [
    path('', index),
    path('cart', cart),
    path('checkout', checkout),

]

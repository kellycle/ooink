from django.urls import path
from . import views

urlpatterns = [
    # Display
    path('', views.dispIndex),
    path('order', views.dispOnlineOrder),
    path('about', views.dispComingSoon),
    path('press', views.dispComingSoon),
    path('gallery', views.dispComingSoon),
    # path('admin', views.dispAdmin)
    # Action
    path('add_to_order', views.add),
    path('increase_quantity/<str:key>', views.increase_quantity),
    path('decrease_quantity/<str:key>', views.decrease_quantity),
    path('clear', views.clear),
    path('checkout', views.checkout),
    path('success/<int:order_id>', views.checkout_success), 
]
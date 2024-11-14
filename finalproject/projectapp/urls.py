from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('user/',views.UserView.as_view(),name='user'),
    path('menu_api/',views.MenuItemView.as_view(),name='menu api'),
    path('menu_api/<int:pk>/',views.SingleMenuItemView.as_view(),name='single menu api'),
    path('booking_api/',views.BookingItemView.as_view(),name='booking api'),
    path('booking_api/<int:pk>/',views.SingleBookingItemView.as_view(),name='single booking api'),
    path('booking/',views.booking,name='booking'),
    path('auth_token/',obtain_auth_token,name='obtain_auth_token'),
]
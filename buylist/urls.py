from .views import *
from django.urls import path

urlpatterns = [
    path('', start, name='start'),
    path('add_item/', add_item, name='add_item'),

    path('auth/login', authorization, name='login'),
    path('auth/register', register, name='register'),
    path('auth/logout', logout_user, name='logout'),
    path('add_category/', add_category, name='add_category'),
    path('filter/<int:days>', filter_by_days, name='filter_days'),

]


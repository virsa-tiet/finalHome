from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.Home,name='Home'),
    path('pre_events',views.pre_events,name='event'),
    path('main_events',views.main_events,name='event'),
    path('online_events',views.online_events,name='event'),
    path('core',views.core,name='core'),
    path('heads',views.heads,name='heads'),
    path('gallery',views.gallery,name='gallery'),
    
]

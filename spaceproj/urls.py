from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('plan', views.plan, name='plan'),
    path('about-us', views.about, name='about'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('booking', views.booking, name='booking'),
]

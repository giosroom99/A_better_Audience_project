from django.urls import path
from .import views

urlpatterns=[
    path('',views.index, name='index'),
    path('presentations',views.presentation_views, name='presentations'),
    path('create_presentation',views.create_presentation_views, name='create_presentation'),
    path('stage',views.stage_view, name='stage'),
    path('register',views.register_view, name='register'),
    path('login',views.login_view, name='login'),
    path('logout', views.logout_view,name='logout'),



]
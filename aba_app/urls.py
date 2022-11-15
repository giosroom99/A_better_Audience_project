from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index, name='index'),
    path('presentations',views.presentation_views, name='presentations'),
    path('create_presentation',views.create_presentation_views, name='create_presentation'),
    path('stage',views.stage_view, name='stage'),
    path('add_stage',views.add_stage_view, name='add_stage'),
    path('register',views.register_view, name='register'),
    path('login',views.login_view, name='login'),
    path('logout', views.logout_view,name='logout'),



]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
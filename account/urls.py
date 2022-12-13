from django.urls import path
from. import views


urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('create_profile/', views.create_profile, name= 'create_profile'),
    path('edit_profile/<int:id>', views.edit_user_profile, name= 'edit_profile'),
    path('view_profile/<int:id>', views.view_profile, name='view_profile'),

]
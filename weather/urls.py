from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("healthy")

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='weather/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('add-favorite/', views.add_favorite, name='add_favorite'),
    path('remove-favorite/<int:pk>/', views.remove_favorite, name='remove_favorite'),
    path('health/', health_check, name='health_check'),
] 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('locations/', views.locations, name="locations"),
    path('viewlocations/<str:pk>/', views.viewlocations, name="viewlocations"),
    path('users/', views.users, name="users"),
    path('admin/auth/user/add/', views.createUsers, name="create_users"),
    path('admin/accounts/entry/add/', views.createLocations, name="create_locations"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user_profile/', views.userProfile, name="profile"),

]
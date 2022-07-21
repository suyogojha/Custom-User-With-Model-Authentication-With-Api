from django.urls import path
from . import views

urlpatterns = [
   # path('', views.landing, name="landing"),
   # path('users/', views.user_index, name="user.index"),
   # path('users/login/', views.user_login, name="user.login"),
   # path('users/create/', views.user_register, name="user.create"),
   # path('users/logout/', views.user_logout, name="user.logout"),

   path('a/', views.cpmreg, name="cpmreg"),
   path('a/<int:id>/', views.cmpregde, name="cmpregde"),


   path('b/', views.cpmlogin, name="cpmlogin"),
   path('b/<int:id>/', views.cpmlogin, name="cpmlogin"),

]
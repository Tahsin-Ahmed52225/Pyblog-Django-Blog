from django.urls import path
from App_login import views
app_name = 'App_login'
urlpatterns = [
 path('sign-up/', views.sign_up, name="sign_up"),
 path('login/', views.login_user, name="login_user"),
 path('logout/', views.logout_user, name="logout_user")
]

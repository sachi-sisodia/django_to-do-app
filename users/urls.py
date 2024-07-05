from django.urls import path
from users import views


urlpatterns = [
      path('signup/', views.sign_up, name="signup"),
      path('login/', views.user_login, name="login"),
      path('logout/', views.user_logout, name="logout"),
]

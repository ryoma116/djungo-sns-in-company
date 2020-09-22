from django.urls import path
from .views import signup_func, login_func, list_func, logout_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('list/', list_func, name='list'),
]

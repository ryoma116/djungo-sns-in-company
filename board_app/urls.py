from django.urls import path
from .views import signup_func, login_func, list_func, logout_func, detail_func, good_func, read_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('list/', list_func, name='list'),
    path('detail/<int:pk>', detail_func, name='detail'),
    path('good/<int:pk>', good_func, name='good'),
    path('read/<int:pk>', read_func, name='read'),
]

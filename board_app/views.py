from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from pprint import pprint

# Create your views here.
from board_app.models import BoardModel


def signup_func(request):

    user2 = User.objects.all()
    pprint(user2)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.create_user(username=username,
                                     password=password)

        except:
            return render(request,
                          template_name='signup.html',
                          context={'error': 'このユーザは登録されています。'})

    return render(request, template_name='signup.html', context={'some': 100})


def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Userの権限取得
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')

    return render(request, template_name='login.html')


@login_required
def list_func(request):
    object_list = BoardModel.objects.all()
    return render(request, template_name='list.html', context={'object_list': object_list})

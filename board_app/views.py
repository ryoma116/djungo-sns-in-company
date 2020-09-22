from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from pprint import pprint

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


def logout_func(request):
    logout(request)
    return redirect('login')


@login_required
def list_func(request):
    object_list = BoardModel.objects.all()
    return render(request, template_name='list.html', context={'object_list': object_list})


@login_required
def detail_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, template_name='detail.html', context={'object': object})


@login_required
def good_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')


@login_required
def read_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    user_ids = object.readtext.split(',')
    user_id = str(request.user.pk)
    if user_id in user_ids:
        return redirect('list')

    object.read += 1
    object.readtext += f',{user_id}'
    object.save()
    return redirect('list')


class BoardCreateView(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'images', 'author')
    success_url = reverse_lazy('list')

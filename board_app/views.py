from django.contrib.auth.models import User
from django.shortcuts import render

from pprint import pprint

# Create your views here.
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

from django.shortcuts import render
from django.views import View
from .models import UserModel, PostModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        data = request.POST
        message_error = dict()
        if len(data) == 4:
            username = data['username']
            password = data['password']
            email = data['email']
            try:
                User.objects.create_user(username=username, password=password, email=email)
            except:
                message_error['message'] = 'User with this name is already registered'
                return render(request, 'login/login.html', context=message_error)
            else:
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/posts')
        elif len(data) == 3:
            username = data['username']
            password = data['password']
            try:
                user = User.objects.get(username=username)
            except:
                message_error['message'] = 'No user with this name found'
                return render(request, 'login/login.html', context=message_error)

            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    return HttpResponseRedirect('/posts')
                else:
                    message_error['message'] = 'Incorrect password'
                    return render(request, 'login/login.html', context=message_error)


class PostView(View):
    def get(self, request):
        posts = PostModel.objects.all()
        data ={
            'posts': posts
        }
        return render(request, 'login/posts.html', context=data)

    def post(self, request):
        data = request.POST
        post = data['post']
        user = request.user
        if user.is_authenticated:
            date_now = str(date.today())
            PostModel.objects.create(user=user, post_text=post, date=date_now)
            return HttpResponseRedirect('/posts')
        else:
            return HttpResponse('Чтобы оставлять посты нужно войти в профиль')


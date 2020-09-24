from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse ,FileResponse ,JsonResponse
import io
from reportlab.pdfgen import canvas
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
import json
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from pyexcel_xlsx import get_data ,save_data
import pandas as pd
# Create your views here.
from .forms import *
from blog.forms import ArticleModelForm
from blog.models import Article

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user=form.save()
        username = form.cleaned_data.get('username')

        group = Group.objects.get(name='profile')
        user.groups.add(group)

        messages.success(request,'user account created for '+ username)
        return redirect('login')

    context ={'form':form}
    return render(request,'dashboard/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('article-home')
        else:
            #return redirect('profile-detail')
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'dashboard/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('article-home')


def profile(request):
    queryset = Profile.objects.all()
    #query = queryset
    context ={
            'objects':queryset
    }
    return render(request,"dashboard/profile.html",context)



def user_list(request):
    queryset = User.objects.all()
    context ={
            'object_list':queryset
    }
    return render(request,"dashboard/user_list.html",context)



def profile_list(request):
    queryset = Profile.objects.all()
    context ={
            'object_list':queryset
    }
    return render(request,"dashboard/profile_list.html",context)

@allowed_users(allowed_roles=['admin'])
def profile_details(request,id):
    obj = get_object_or_404(Profile, id=id)
    obj = Profile.objects.get(id=id)
    try:
        if request.method == "POST":
            obj = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        raise Http404
    context ={
            'object':obj
    }
    return render(request,"dashboard/profile_detail.html",context)

def user_update(request,id):
    user=User.objects.get(id=id)
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'user account updated for '+ user)
            return redirect('login')
    context ={'form':form}
    return render(request,'dashboard/user_update.html',context)


def user_delete(request,id):
        obj = get_object_or_404(User, id=id)
        if request.method == "POST":
            obj.delete()
            return redirect('../../')
        context ={
                'object':obj
        }
        return render(request,"dashboard/user_delete.html",context)


def profile_delete(request,id):
        obj = get_object_or_404(Profile, id=id)
        if request.method == "POST":
            obj.delete()
            return redirect('profile-list')
        context ={
                'object':obj
        }
        return render(request,"dashboard/user_delete.html",context)



@allowed_users(allowed_roles=['profile','admin'])
def profile_settings(request):
    customer = request.user.profile
    form = userForm(instance=customer)
    if request.method == 'POST':
        form = userForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form':form}
    return render(request, 'dashboard/profile_settings.html', context)


@api_view(['GET'])
def downloadExcel(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    data= pd.DataFrame(serializer.data)
    print(data.head())
    data.to_excel(r"profiles.xlsx",index=False)
    return Response(serializer.data)

@api_view(['GET'])   
def some_view(request):
    # Create a file-like buffer to receive PDF data.
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    data= pd.DataFrame(serializer.data)
    return Response(serializer.data)

def home(request):
    return render(request,'home.html')


def ArticleListView2(request):
    queryset= Article.objects.all()
    context ={
            'object_list':queryset
    }
    return render(request,'article.html',context)

def about(request):
    return render(request,'About.html')
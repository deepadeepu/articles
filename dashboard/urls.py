from django.contrib import admin
from django.urls import path,include
from . import views


#app_name='dashboard'

urlpatterns = [
    path('register/', views.registerPage,name='register'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutUser,name='logout'),



    path('user_list', views.user_list,name='user_list'),
    path('user_update/<int:id>/', views.user_update,name='user_update'),
    path('user-delete/<int:id>/', views.user_delete,name='user-delete'),
    #path('user-delete/<int:id>/', views.user_delete,name='user-delete'),
    path('profile/', views.profile,name='profile'),
    path('profile-list/', views.profile_list,name='profile-list'),
    path('profile-detail/<int:id>/', views.profile_details,name='profile-detail'),
    path('profile-delete/<int:id>/', views.profile_delete,name='profile-delete'),
    path('profile-settings/',views.profile_settings,name='profile-settings'),
    path('excel/',views.downloadExcel,name='excel'),
    path('pdf/',views.some_view,name='pdf'),
    
    path('article',views.ArticleListView2, name ='article'),
    path('about/',views.about, name ='about'),

]

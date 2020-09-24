from django.urls import path
from .views import *

urlpatterns = [
    path('article-create/', ArticleCreateView.as_view(),name='article-create'),
    path('article-list', ArticleListView.as_view(),name='article-list'),
    path('article-detail/<int:id>/', ArticleDetailView.as_view(), name ='article-detail'),
    path('article-update/<int:id>/', ArticleUpdateView.as_view(), name ='article-update'),
    path('article-delete/<int:id>/', ArticleDeleteView.as_view(), name ='article-delete'),
    path('article-titles', ArticleListView2.as_view(), name ='article-titles'),
    path('article-api', articlesApi, name ='article-api'),
    path('article-detail-api/<int:pk>/', articleDetailApi, name ='article-detail-api'),
     path('', ArticleListViewHome.as_view(), name ='article-home'),
     path('article-admin', ArticleListViewHome2.as_view(), name ='article-admin'),

    ]
# app_name= 'articles'
# urlpatterns = [
#             path('', ArticleListView.as_view(), name ='article-list'),
#             path('create/', ArticleCreateView.as_view(), name ='article-create'),
#             path('<int:id>/', ArticleDetailView.as_view(), name ='article-detail'),
#             path('<int:id>/update/', ArticleUpdateView.as_view(), name ='article-update'),
#             path('<int:id>/delete/', ArticleDeleteView.as_view(), name ='article-delete')

# ]

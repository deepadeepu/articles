from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.views.generic import(
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView)

from .forms import ArticleModelForm
from .models import Article
import json
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

class ArticleCreateView(CreateView):
    template_name='articles/article_create.html'
    form_class=ArticleModelForm
    queryset= Article.objects.all()
    #success_url = '/'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    


    # def get_success_url(self):
    #     return '/'

class ArticleListView(ListView):
    template_name='articles/article_list.html'
    queryset= Article.objects.all()



class ArticleDetailView(DetailView):
    template_name='articles/article_detail.html'
    queryset= Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)


class ArticleUpdateView(UpdateView):
    template_name='articles/article_create.html'
    form_class=ArticleModelForm
    queryset= Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name='articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

    def get_success_url(self):
        return reverse("article-list")

@api_view(['GET'])
def articlesApi(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def articleDetailApi(request,pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles, many=False)
    return Response(serializer.data)


class ArticleListView2(ListView):
    template_name='articles/article_list_titles.html'
    queryset= Article.objects.all()


class ArticleListViewHome(ListView):
    template_name='articles/article.html'
    queryset= Article.objects.all() 

class ArticleListViewHome2(ListView):
    template_name='articles/article-admin.html'
    queryset= Article.objects.all() 
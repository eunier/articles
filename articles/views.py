from django.views.generic import ListView, DetailView

from . models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'article_list_view'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article_detail_view'


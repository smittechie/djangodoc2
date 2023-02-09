from time import timezone

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView , DetailView

from .models import Publisher, Book, Author


class AboutView(TemplateView):
    template_name = 'cbv/about.html'

class MyView(View):
    def get (self,request):
        return HttpResponse('result')

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'      ##for data fetching as


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()              ## it is equal to model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context

class AcmeBookListView(ListView):

    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'books/acme_list.html'

class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
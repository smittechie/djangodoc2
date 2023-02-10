from datetime import datetime
from django.urls import reverse_lazy
from time import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import ContactForm
from .models import Publisher, Book, Author


class AboutView(TemplateView):
    template_name = 'cbv/about.html'


class MyView(View):
    def get(self, request):
        return HttpResponse('result')


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'  ##for data fetching as


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()  ## it is equal to model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class AcmeBookListView(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'books/acme_list.html'


class PublisherBookListView(ListView):
    template_name = 'cbv/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        context['publisher1'] = Publisher.objects.all()
        print(self.publisher)
        print(context['publisher1'])
        return context


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    context_object_name = 'author'

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = datetime.now()
        obj.save()
        return obj


def Thanks(request):
    return HttpResponse("thanks")


class ContactViewForm(FormView):
    template_name = 'cbv/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('cbv:thanks')

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.all()
    template_name = 'cbv/author_list.html'


class AuthorCreateView(CreateView):
    """

    """
    model = Author
    fields = ['name']
    template_name = 'cbv/author_detail.html'
    success_url = reverse_lazy('cbv:thanks')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']
    template_name = 'cbv/author_updata.html'
    success_url = reverse_lazy('cbv:thanks')


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('cbv:thanks')
    template_name = 'cbv/author_confirm_delete.html'
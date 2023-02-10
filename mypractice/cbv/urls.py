from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from .views import AboutView, MyView, PublisherListView, AuthorDetailView, PublisherBookListView, ContactViewForm, \
    AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorListView

app_name = 'cbv'

urlpatterns = [
    path('', AboutView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
    path("home/", TemplateView.as_view(template_name='registration/home.html'), name='home'),
    path('about/', MyView.as_view()),
    path('publishers/', PublisherListView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/<publisher>/', PublisherBookListView.as_view()),
    path('ContactForm/', ContactViewForm.as_view()),
    path('thanks/', views.Thanks, name='thanks'),
    path('author/list/', AuthorListView.as_view(), name='author-list'),
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]

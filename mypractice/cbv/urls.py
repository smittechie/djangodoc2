from django.urls import path
from .views import AboutView, MyView, PublisherListView, AuthorDetailView

app_name = 'cbv'

urlpatterns = [
    path('', AboutView.as_view()),
    path('about', MyView.as_view()),
    path('publishers', PublisherListView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail')
]

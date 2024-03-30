from django.urls import path
from .views import get_wikipedia_summary,test_email

urlpatterns = [
    path('summary/', get_wikipedia_summary, name='summary'),
    path('email/', test_email, name='email'),
]

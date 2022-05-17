from django.urls import path
from .views import *


urlpatterns = [
    path('artists/', ArtistPage.as_view()),
    path('biography/<name>', BiographyPage.as_view(), name='biography'),
]
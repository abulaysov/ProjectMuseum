from django.urls import path
from .views import *


urlpatterns = [
    path('pictures/', PicturesPage.as_view()),
    path('picture/<name>', PicturePage.as_view(), name='picture')
]
from .views import *
from django.urls import path


urlpatterns = [
    path('', MainPage.as_view()),
    path('about/', AboutPage.as_view())
]

handler404 = "mainpage.views.page_not_found_view"
from django.shortcuts import render, redirect
from django.views import View
from .models import Quotes
from random import sample


class MainPage(View):
    def get(self, request, *args, **kwargs):
        img_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12']
        data = list(Quotes.objects.all())
        data = sample(data, 3)
        img_list = sample(img_list, 3)
        return render(request, 'mainpage/mainpage.html', context={'quote_1': data[0],
                                                                    'quote_2': data[1],
                                                                    'quote_3': data[2],
                                                                    'img1': img_list[0],
                                                                    'img2': img_list[1],
                                                                    'img3': img_list[2]})


class AboutPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainpage/about.html')


def page_not_found_view(request, exception):
    return render(request, 'mainpage/404.html', status=404)
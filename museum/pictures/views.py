from django.shortcuts import render
from django.views import View
from .models import Pictures
from random import shuffle


class PicturesPage(View):
    def get(self, request, *args, **kwargs):
        picture_name = request.GET.get('picture_name')
        search_list = []
        data = list(Pictures.objects.all())
        if picture_name:
            for i in data:
                if picture_name.lower() in str(i.name_picture).lower():
                    search_list.append(i)
                elif picture_name.lower() in str(i.author.author_name).lower().split():
                    search_list.append(i)
                elif picture_name.lower() in str(i.genre.genre_name).lower().split():
                    search_list.append(i)
                elif picture_name.lower() in str(i.location).lower().replace(' ', '').split(','):
                    search_list.append(i)
            if any(search_list):
                return render(request, 'pictures/pictures.html', context={'data': search_list})
            else:
                return render(request, 'pictures/pictures.html', context={'notfound': True, 'inp': picture_name})

        genre = request.GET.get('genre')
        author = request.GET.get('author')
        location = request.GET.get('location')
        picture = request.GET.get('picture')
        if genre or location or picture or author:
            if genre == 'Все' and location == '' and picture == '' and author == '':
                ...
            else:
                for i in data:
                    if genre != 'Все' and genre in str(i.genre):
                        if author != '' and author.lower() not in str(i.author.author_name).lower().split():
                            continue
                        if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
                            continue
                        if picture != '' and picture.lower() not in str(i.name_picture).lower():
                            continue
                        search_list.append(i)
                    elif genre == 'Все':
                        if author != '' and author.lower() not in str(i.author.author_name).lower().split():
                            continue
                        if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
                            continue
                        if picture != '' and picture.lower() not in str(i.name_picture).lower():
                            continue
                        search_list.append(i)
                if any(search_list):
                    return render(request, 'pictures/pictures.html', context={'data': search_list})
                else:
                    return render(request, 'pictures/pictures.html', context={'notfound': True})

        # if len(search_list) == 0 and len(str(picture_name)) > 0 and picture_name is not None:
        #     if len(str(picture_name)) > 10:
        #         picture_name = picture_name[:10] + '...'
        #     return render(request, 'pictures/pictures.html', context={'data': data, 'search': False, 'inp': picture_name})
        shuffle(data)
        return render(request, 'pictures/pictures.html', context={'data': data})


class PicturePage(View):
    def get(self, request, name, *args, **kwargs):
        return render(request, 'pictures/picture.html', context={'data': Pictures.objects.filter(id=name)})
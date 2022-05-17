from django.shortcuts import render
from django.views import View
from .models import Biographies
from random import shuffle


class ArtistPage(View):
    def get(self, request, *args, **kwargs):
        name_artist = request.GET.get('name_artist')
        search_list = []
        data = list(Biographies.objects.all())
        if name_artist:
            for i in data:
                if name_artist.lower() in i.name.lower().split():
                    search_list.append(i)
                elif name_artist.lower() in i.era.lower().split():
                    search_list.append(i)
                elif name_artist.lower() in i.genre.lower().split():
                    search_list.append(i)
                elif name_artist.lower() in i.location.lower().replace(' ', '').split(','):
                    search_list.append(i)
            if any(search_list):
                return render(request, 'artists/artists.html', context={'set': search_list})
            else:
                return render(request, 'artists/artists.html', context={'notfound': True})
        # genre = request.GET.get('genre')
        author = request.GET.get('author')
        location = request.GET.get('location')
        era = request.GET.get('era')

        if location or era or author:
            if location == '' and era == 'Все' and author == '':
                shuffle(data)
                return render(request, 'artists/artists.html', context={'set': data})
            else:
                for i in data:
                    if era != 'Все' and era.lower() in str(i.era).lower():
                        if author != '' and author.lower() not in str(i.author.author_name).lower().split():
                            continue
                        if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
                            continue
                        search_list.append(i)
                    elif era == 'Все':
                        if author != '' and author.lower() not in str(i.author.author_name).lower().split():
                            continue
                        if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
                            continue
                        search_list.append(i)
                if any(search_list):
                    return render(request, 'artists/artists.html', context={'set': search_list})
                else:
                    return render(request, 'artists/artists.html', context={'notfound': True})

        shuffle(data)
        return render(request, 'artists/artists.html', context={'set': data})
    

class BiographyPage(View):
    def get(self, request, name, *args, **kwargs):
        return render(request, 'artists/biography.html', context={'bio': Biographies.objects.filter(id=name)})


#                                   IF THE GENRE IS IN THE FILTERS
# if (genre != 'Все' and genre in str(i.genre)) and (era != 'Все' and era.lower() in str(i.era).lower()):
#     if author != '' and author.lower() not in str(i.author.author_name).lower().split():
#         continue
#     if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
#         continue
#     search_list.append(i)
# elif (genre == 'Все') and (era != 'Все' and era.lower() in str(i.era).lower()):
#     if author != '' and author.lower() not in str(i.author.author_name).lower().split():
#         continue
#     if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
#         continue
#     search_list.append(i)
# elif (genre != 'Все' and genre in str(i.genre)) and (era == 'Все'):
#     if author != '' and author.lower() not in str(i.author.author_name).lower().split():
#         continue
#     if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
#         continue
#     search_list.append(i)
# elif genre == 'Все' and era == 'Все':
#     if author != '' and author.lower() not in str(i.author.author_name).lower().split():
#         continue
#     if location != '' and location.lower() not in str(i.location).lower().replace(' ', '').split(','):
#         continue
#     search_list.append(i)

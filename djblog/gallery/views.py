from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Album, Photo

@login_required
def home(request):
    albums = Album.objects.filter(user=request.user)
    data = {"albums": albums}
    return render(request, 'gallery/index.html', data)


@login_required
def add_album(request):
    data = {}
    return render(request, 'gallery/add_album.html', data)


@login_required
def show_album(request, pk):
    album = Album.objects.get(id=pk)
    photos = Photo.objects.filter(album=album)
    data = {"album": album, "photos": photos}
    return render(request, 'gallery/show_album.html', data)

@login_required
def save_album(request):
    data = {}
    title = request.POST["title"]
    description = request.POST["description"]
    album = Album(user=request.user, title=title, description=description, img=request.FILES['img'])
    album.save()

    albums = Album.objects.filter(user=request.user)
    data = {"albums": albums}
    return render(request, 'gallery/index.html', data)

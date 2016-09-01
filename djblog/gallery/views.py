from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Album, Photo
from .forms import AlbumForm, CategoryForm, PhotoForm

def main(request):
    """Main listing."""
    albums = Album.objects.all()
    photos = Photo.objects.all()

    paginator = Paginator(albums, 5)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.photos = album.photos()[:4]

    return render(request, "list-recent.html", dict(albums=albums, photos=photos, user=request.user,
        media_url=MEDIA_URL))

@login_required
def home(request):
    albums = Album.objects.filter(user=request.user)
    data = {"albums": albums}
    return render(request, 'gallery/index.html', data)

@login_required
def add_album(request):
    if request.method == "GET":
        album = AlbumForm()
    else:
        album = AlbumForm(request.POST)
        if album.is_valid():
            obj = album.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/')

    data = {'form': album}
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

@login_required
def add_photo(request, pk):
    album = Album.objects.get(id=pk)

    data = {'album': album}
    return render(request, 'gallery/add_photo.html', data)

@login_required
def save_photo(request):
    data = {}
    caption = request.POST["caption"]
    public = request.POST["public"]
    public=True if public==1 else False

    aid = request.POST["album"]
    album = Album.objects.get(id=aid)
    photo = Photo(user=request.user, album=album, caption=caption, public=public, img=request.FILES['img'])
    photo.save()

    albums = Album.objects.filter(user=request.user)
    data = {"albums": albums}
    return render(request, 'gallery/index.html', data)

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Book
from .forms import BookUpload

#from rest_framework import viewsets
#from .serializers import BookSerializer


def index(request):
    try:
        books = Book.objects.all()
    except Book.DoesNotExist:
        books = None

    return render(request, 'bookLibrary/index.html', {'books': books})


"""
# for View Rest API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""


def upload(request):
    if request.method == 'POST':
        book_form = BookUpload(data=request.POST)
        if book_form.is_valid():
            bf = book_form.save(commit=False)

            if 'cover_image' in request.FILES:
                bf.cover_image = request.FILES['cover_image']
            bf.save()

            return redirect(reverse('BookLibrary:home'))

        return HttpResponse(request, "Invalid Form!!")

    book_form = BookUpload()
    return render(request, 'bookLibrary/upload.html', {'form': book_form})


def edit(request, id):
    book_id = int(id)
    try:
        book_upd = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('BookLibrary:home')

    book_form = BookUpload(request.POST or None, instance=book_upd)
    if book_form.is_valid():
        book_form.save()
        return redirect('BookLibrary:home')
    return render(request, 'bookLibrary/upload.html', {'form': book_form})


def book_delete(request, id):
    book_id = int(id)
    try:
        book_del = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('BookLibrary:home')

    book_del.delete()
    return redirect('BookLibrary:home')

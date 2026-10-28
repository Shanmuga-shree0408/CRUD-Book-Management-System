from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# 1. Read (View all books)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'management/book_list.html', {'books': books})

# 2. Create (Add new book)
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'management/book_form.html', {'form': form})

# 3. Update (Edit existing book)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'management/book_form.html', {'form': form})

# 4. Delete (Remove book)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'management/book_confirm_delete.html', {'book': book})

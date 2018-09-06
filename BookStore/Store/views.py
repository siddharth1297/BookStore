from django.shortcuts import render, HttpResponse
from .forms import BookForm
from .models import Book, Tag


# Create your views here.
def index(request):
    upload_status = None
    upload_msg = None

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            name = request.FILES['file'].name
            description = request.POST['description']
            tags = data['tags']
            tag_list = tags.split('-')
            try:
                b = Book(name=name, description=description, document=request.FILES['file'])
                b.save()
                for i in tag_list:
                    Tag(book_id=b, tag=str(i)).save()

                upload_status = 'Success'
                upload_msg = 'updated successfully'
            except:
                print("Except   ")
                upload_status = 'Fail'
                upload_msg = 'Book with same name exist, Try with some other name'
        else:
            return HttpResponse('Error in validation')

    form = BookForm()

    all_tags = Tag.objects.all().order_by('tag')
    tag_choices = []

    try:
        last_book = Book.objects.all().order_by('uploaded_at')
        last_book_time = last_book[0].uploaded_at
    except:
        last_book_time = "No Books"

    for tag in all_tags:
        tag_choices.append(tag.tag)

    tags = {}
    for tag in tag_choices:
        book_with_tag = Tag.objects.filter(tag=tag)
        book_list = []

        for book in book_with_tag:
            t = Book.objects.filter(id=book.book_id.id)
            for i in t:
                book_list.append(i)
        tags[tag] = book_list

    if upload_status is None:
        upload_status = 'Primary'
        upload_msg = 'last updated: ' + str(last_book_time)

    return render(request, 'index.html', {'form': form, 'tags': tags, 'upload_status': upload_status, 'upload_msg': upload_msg})

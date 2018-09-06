from django.shortcuts import render, HttpResponse, redirect
from .forms import BookForm
from .models import Book, Tag

# Create your views here.
def index(request):
    upload_msg = None
    upload_status = None
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            #print(data)
            name = request.FILES['file'].name
            #subject = request.POST['subject']
            description = request.POST['description']

            #b = Book(name=name, subject=subject, description=description, document=request.FILES['file'])
            try:
                b = Book(name=name, description=description, document=request.FILES['file'])
                tags = data['tags']
                b.save()
                for i in tags:
                    Tag(book_id=b, tag=str(i)).save()
            except:
                print("Except   ")
                upload_status = "Fail"
                upload_msg = "Book with same name exist, Try with some other name"
                redirect(index)
            finally:
                upload_status = "Fail"
                upload_msg = "Book with same name exist, Try with some other name"
                redirect(index)
            upload_status = "Success"
            upload_msg = "updated successfully"
            redirect(index)
        else:
            return HttpResponse('Error in validation')
    form = BookForm()
    docs = Book.objects.all()

    tag_choice = ['Computer Architecture', 'Operating System', 'Networking', 'Distributed System', 'Machine Learning',
                  'Deep Learning', 'Artificial Intelligence', 'Algorithm', 'Theoretical CS']
    tags = {}
    for tag in tag_choice:
        #print(tag)
        book_with_tag = Tag.objects.filter(tag=tag)
        book_list = []

        for book in book_with_tag:
            #print('\t' + str(book.book_id.id) + '\t' + str(book.tag))
            t = Book.objects.filter(id=book.book_id.id)
            for i in t:
                book_list.append(i)
        tags[tag] = book_list
    #print(tags)
    if upload_status is None:
        upload_status = 'Primary'
        upload_msg = 'last updated: '
    print(upload_status)
    return render(request, 'model_form_upload.html', {'form': form, 'tags': tags, 'upload_status': upload_status, 'upload_msg': upload_msg})


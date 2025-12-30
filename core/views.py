from django.shortcuts import render, redirect
from .models import Bookmarks
from django.contrib.auth.decorators import login_required

@login_required
def bookmarksList(request):
    user =request.user
    bookmarks = Bookmarks.objects.filter(user=user)
    return render(request, 'bookmarks-list.html',{'bookmarks':bookmarks})

@login_required
def addBookmark(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('link')
        category = request.POST.get('category')
        description = request.POST.get('description')
        user=request.user
        
        b=Bookmarks()
        if not title:
            b.title=link
        else:
            b.title=title
        b.link=link
        b.category=category
        b.description=description
        b.user=user

        b.save()
        return redirect('bookmarksList')
    return render(request, 'input-form.html')

def deleteBookmark(request,id):
    bookmark=Bookmarks.objects.get(id=id)
    bookmark.delete()
    return redirect('bookmarksList')

def editBookmark(request, id):
    b=Bookmarks.objects.get(id=id)
    if request.method=='POST':
        b.title=request.POST.get('title')
        b.link=request.POST.get('link')
        b.category=request.POST.get('category')
        b.description=request.POST.get('description')
        b.save()
        return redirect('bookmarksList')
    else:
        if not b:
            return redirect('bookmarkLists')
        bookmark={
            'id':b.id,
            'title':b.title,
            'link':b.link,
            'category':b.category,
            'description':b.description,

        }
        return render(request,'edit-form.html',{'bookmark':bookmark})
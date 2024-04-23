from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from book.models import *


def hello(req):
    return  HttpResponse("<h1>Hello Django</h1>")


def book_list(req):
    #return HttpResponse("<h1>Book_List</h1>")
    context={}
    books=Book.objects.all()
    context['books']=books
    return render(req,'book/list.html',context)

def book_add(req):
    # return HttpResponse("<h1>Book_Add</h1>")
    return render(req,'book/add.html')

def book_details(req,id):
     # return HttpResponse(f"<h1>{id}_detailes</h1>")
    context={}
    book=Book.objects.get(id=id)
    context['book']=book
    return render(req,'book/detailes.html',context)
def book_delete(req,id):
    Book.objects.filter(id=id).delete()
    return redirect('book_list')
    # return HttpResponse(f"<h1>Book-delete-{id}</h1>")

def book_update(req,id):
    return HttpResponse("<h1>Book-{id}-updated</h1>")
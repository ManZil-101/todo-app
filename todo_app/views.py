from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from todo_app.models import Todo

# Create your views here.
def index(request):
    notes= Todo.objects.all()
    return render(request, 'todo_app/home.html', context= {'notes' : notes})

def delete(request,id):
    note =Todo.objects.get(id=id)
    note.delete()
    return redirect('index')

def add(request):
    if request.method == 'GET':
        return render(request, 'todo_app/add.html')
    else:
        title = request.POST['title']
        description= request.POST['description']
        Todo.objects.create(title=title, description=description)
        return redirect('index')


def edit(request,id):
    note = Todo.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'todo_app/edit.html', {'note':note})
    else:
       
        note.title = request.POST['title']
        note.description = request.POST['description']
        note.save()
        return redirect('index')


def is_completed(request, id):
    note = Todo.objects.get(id=id)
    
    note.is_completed= not note.is_completed
    note.save()
    return redirect('index')


    
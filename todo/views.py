from django.shortcuts import render,redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
# Create your views here.

def  todolist(request):
    form = TodoForm()
    objects = Todo.objects.all()
    context = {'todolist':objects,'todoform':form}
    return render(request,'todo/index.html',context)


def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            new_todo = Todo(title=title)
            new_todo.save()
            redirect('todo_list')          
    else:
        form = TodoForm()
    objects = Todo.objects.all()
    context = {'todolist':objects,'todoform':form}
    return render(request,'todo/index.html',context)
        
        
def update(request):
    todo = Todo.objects.get(pk=request.POST.get('id'))
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('todo_list')
    
    else:         
        form = TodoForm()
    objects = Todo.objects.all()
    context = {'todolist':objects,'todoform':form}
    return render(request,'todo/index.html',context)
        

def delete(request):
    obj = get_object_or_404(Todo,pk=request.POST.get('id'))
    if request.method == 'POST':
        obj.delete()
        return redirect('todo_list')
    
    else:         
        form = TodoForm()
    objects = Todo.objects.all()
    context = {'todolist':objects,'todoform':form}
    return render(request,'todo/index.html',context)
        
    
    
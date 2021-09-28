from django.shortcuts import render, redirect
from .models import Item  # Allows us to use the Item model in our views


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    # Above line creates a query set of all the items in the database
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
    # above line injects the request and context data into
    # the todo_list template.


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')

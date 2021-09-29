from django.shortcuts import render, redirect
from .models import Item  # Allows us to use the Item model in our views
from .forms import ItemForm


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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

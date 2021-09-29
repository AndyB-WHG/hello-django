from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # 'get_object_or_404 imported on top line.
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    form = ItemForm(instance=item)  # 'item' variable taken from two lines above.
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # 'get_object_or_404 imported on top line.
    item.done = not item.done  # Flips the status of Done/Not done to the opposite of it's current value.
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # 'get_object_or_404 imported on top line.
    item.delete()
    return redirect('get_todo_list')

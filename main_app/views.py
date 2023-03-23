from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def home(request):
    widget_form = WidgetForm    
    data = Widget.objects.all()
    return render(request, 'home.html', {'form': widget_form,
                                         'data': data})

def form(request):
    if request.method == 'POST':
        Widget.objects.create(description=request.POST['description'], quantity=request.POST['quantity'])
        return redirect('/')
    
def delete_item(request, widget_id):
    Widget.objects.get(pk=widget_id).delete()
    return redirect('/')
  
from django.shortcuts import render, redirect, HttpResponse

from item.models import Category, Item
from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'items': items,
    }

    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("success")
    else:
        form = SignupForm()
        
    context = {
        'form': form,
    }
    
    return render(request, 'core/signup.html', context)

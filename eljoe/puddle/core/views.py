from django.shortcuts import render, redirect
# Create your views here.

from item.models import Category, Item

from .forms import Signupform

def index(request):
    items = Item.objects.filter(is_sold = False)
    # items = Item.objects.filter(is_sold = False)[0:6]
    categ = Category.objects.all()
    return render(request, 'static/index.html', {
        'categories': categ,
        'items': items,
    })

def contact(requset):
    return render(requset, 'static/contact.html')

def signup(request):

    if request.method =='POST':
        form = Signupform(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login/')
        
    else:
        form = Signupform()

    return render(request, 'static/signup.html', {
        'form': form,
    })
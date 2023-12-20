from django.shortcuts import get_object_or_404, render

from django.contrib.auth.decorators import login_required

from item.models import Item, Category

# Create your views here.

def index (request):
    items = Item.objects.filter(created_by=request.user)
    categ = Category.objects.all()

    return render(request, 'static/dashboard_index.html', {
        'items': items,
        'categories': categ,
    })


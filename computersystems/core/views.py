from django.shortcuts import render
from item.models import Category, Laptop
def index(request):
     laptops = Laptop.objects.all()
     categories = Category.objects.all()
     return render(request, 'core/index.html',
                   {'categories':categories,
                    'laptops':laptops,
                   }
                   )

def contact(request):
     return render(request, 'core/contact.html')
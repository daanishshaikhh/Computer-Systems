from django.shortcuts import render, get_object_or_404
from .models import Laptop
def detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'laptop/detail.html', {
        'laptop': laptop
    })
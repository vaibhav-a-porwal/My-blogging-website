# from django.http import HttpResponse
from django.shortcuts import render
from .models import Poem

# Create your views here.
def show_poems(request):
    poems = Poem.objects.all()
    return render(request, 'poems/poems.html', {'poems':poems})

from django.shortcuts import render,redirect
from PyDictionary import PyDictionary

# Create your views here.


def index(request):


    return render(request, 'index.html', )

def dict(request):
    word = request.GET.get('word')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)
    context = {

        'meaning': meaning
    }

    return render(request, 'dict.html', context)
    return redirect('/')

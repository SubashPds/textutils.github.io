# This file is created by me

from django.http import HttpResponse
# to use template
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def removepunc(request):
    # get text from index.html
    text = request.GET.get('text', 'default')
    print(text)
    # Removing punctuation from text

    removepuncstatus = request.GET.get('removepunc', 'off')
    caps = request.GET.get('caps', 'off')
    newlineremover= request.GET.get('newlineremover','off')

    print(removepuncstatus)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepuncstatus == "on":
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    elif (caps == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'capitalized', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char != "\n":
                analyzed = analyzed + char.strip()

            params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("ERROR")


def capitalize(request):
    return HttpResponse('''Capitalize
                                <br>
                                <a href="."><button>Back</button></a>
                            ''')


def newlineremover(request):
    return HttpResponse('''Remove new line
                                <br>
                                <a href="."><button>Back</button></a>
                            ''')


def spaceremove(request):
    return HttpResponse('''space remover
                                <br>
                                <a href="."><button>Back</button></a>
                            ''')


def charcount(request):
    return HttpResponse('''charcount
                                <br>
                                <a href="."><button>Back</button></a>
                            ''')

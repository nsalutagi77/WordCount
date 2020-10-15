from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlength = fulltext.split()

    worddic = {}

    for word in wordlength:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    
    sortedword = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext , 'count':len(wordlength), 'sortedword':sortedword })

def about(request):

    return render(request, 'about.html')
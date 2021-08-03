from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
 #   return HttpResponse("<h1> RAFAY</h1>")
#def about(request):
 #   return HttpResponse("About rafay bhai")
#def contact(request):
 #    return HttpResponse("<h1> please contact the rafay bhai</h1>")
def index(request):
    #params = {'name':'rafay','place':'pakistan','rollno':'78','Gender':'male'}

    return render(request,'index.html')
   #return HttpResponse('home')
def analyze(request):
    djtext= request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc=="on":
   # analyze=djtext
        punctuation=''',./;' '''
        analyze=""
        for char in djtext:
            if char not in punctuation:
                analyze= analyze + char
        params={'purpose':'REMOVEPUNCTUATION','analyze_text':analyze}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")

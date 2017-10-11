
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'session_app/index.html')

def addWord(request):
    newWord = {}

    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "showBig":
            newWord[key] = value
        if key == "showBig":
            newWord['big'] = "big"
        else:
            newWord['big'] = ""
    newWord['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.append(newWord)
    request.session['words'] = temp_list
    for key, val in request.session.__dict__.iteritems():
        print key, val
    print "past created at", newWord

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
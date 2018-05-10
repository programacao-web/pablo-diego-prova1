from django.shortcuts import render, get_object_or_404
from .forms import PastebinForms
from .models import Paste
from django.http import HttpResponseRedirect

def index(request):
    form = PastebinForms()
    ctx = {"form": form}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    ctx = {"pastebin": Paste.objects.get(id=id)}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    pastes = Paste.objects.filter(language=language.upper())
    print(pastes.__dict__)
    ctx = {'pastes': pastes,
           'language':language}
    return render(request, 'pastebin/paste-language.jinja2', ctx)



def create_paste(request):
    print("ASSDDAS")
    if request.method == "POST":
        print("ASSDDAS")
        print(request.__dict__)
        form = PastebinForms(request.POST)
        if form.is_valid:    
            new_paste_bin = form.save()
            print(new_paste_bin.__dict__)
            return HttpResponseRedirect(f'/pastes/{new_paste_bin.id}')   
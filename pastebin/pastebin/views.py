from django.shortcuts import render, get_object_or_404
from .forms import PastebinForms
from django.http import HttpResponseRedirect

def index(request):
    form = PastebinForms()
    ctx = {"form": form}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    ctx = {}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    ctx = {'pastes': []}
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
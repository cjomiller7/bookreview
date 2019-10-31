from django.shortcuts import render, get_object_or_404, redirect  # call this to render a template
from . models import Rev
from . forms import RevForm, BrowForm
from django.db.models import Q


def index(request):  # created a function called index that takes requests and return value from calling function render
    revs = Rev.objects.all()
    return render(request, 'review/index.html',  # render puts together the template review/index.html
                  {'revs': revs})  # dictionary allows for dynamic templates


def rev_detail(request, pk):  #  Used this view for the title link to display on seperate page
    revd = get_object_or_404(Rev, pk=pk)
    return render(request, 'review/rev_detail.html',
                  {'revd': revd})


def new(request):
    if request.method == "POST":
        form = RevForm(request.POST)
        if form.is_valid():
            rev = form.save()
            return redirect('rev_detail', pk=rev.pk)
    else:
        form = RevForm()
    return render(request, 'review/new.html',
                  {'form': form})


def rev_edit(request, pk):
    post = get_object_or_404(Rev, pk=pk)
    if request.method == "POST":
        form = RevForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('rev_detail', pk=post.pk)
    else:
        form = RevForm(instance=post)
    return render(request, 'review/rev_edit.html', {'form': form})




def sci_fi(request):
    sci = Rev.objects.filter(genre="Sci-fi")
    return render(request, 'review/sci.html',
                  {'sci': sci})


def children(request):
    chi = Rev.objects.filter(genre="Children")
    return render(request, 'review/chi.html',
                  {'chi': chi})


def mystery(request):
    mys = Rev.objects.filter(genre="Mystery")
    return render(request, 'review/mys.html',
                  {'mys': mys})


def horror(request):
    hor = Rev.objects.filter(genre="Horror")
    return render(request, 'review/hor.html',
                  {'hor': hor})


#  In Dvelopment


def search(request):
    template = "review/browse.html"

    query = request.GET.get('q')

    results = Rev.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) ) #&

    return render(request, template)

def browse(request):
    if request.method == 'POST':
        form = BrowForm(request.POST)
        request.POST.get('genre')

    else:
        return render(request, 'review/browse.html',)
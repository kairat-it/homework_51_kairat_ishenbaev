from django.shortcuts import redirect, get_object_or_404, render
from .models import Cat
from .forms import InteractForm, GreetForm


def greet(request):
    if request.method == 'POST':
        form = GreetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = Cat.objects.create(name=name)
            return redirect('cat_info')
    else:
        form = GreetForm()

    return render(request, 'greet.html', {'form': form})


def cat_info(request):
    cat = get_object_or_404(Cat, pk=1)
    if request.method == 'POST':
        form = InteractForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            if action == 'feed':
                cat.feed()
            elif action == 'play':
                cat.play()
            elif action == 'sleep':
                cat.sleep()
            return redirect('cat_info')
    else:
        form = InteractForm()

    return render(request, 'cat_info.html', {'cat': cat, 'form': form})


def cat_info_redirect(request):
    return redirect('cat_info')

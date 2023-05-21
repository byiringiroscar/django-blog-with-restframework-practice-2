from django.shortcuts import render, get_object_or_404, redirect
from Sport.models import Statistic
from Sport.forms import SportForm, CommentForm

from django.contrib import messages


# Create your views here.


def info(request):
    information = Statistic.objects.all()
    context = {
        'inform': information
    }
    return render(request, 'html/info.html', context)


def detail(request, id):
    informat = get_object_or_404(Statistic, pk=id)
    # comments = informat.comments.all()
    #
    # form = SportForm(request.POST or None,instance=informat)
    #
    # if form.is_valid():
    #     instance = form.save(commit=False)
        # instance.post = informat
        # instance.body = 'THIS IS THE COMMENT'
        # instance.save()
        # form = SportForm()
        # messages.success(request, 'succesfully')

    context = {
        'informa': informat,
        # 'form': form,
        # 'comments': comments

    }
    return render(request, 'html/detail.html', context)


def publish(request):
    form = SportForm(request.POST or None, request.FILES)

    if form.is_valid():
        # data=form.cleaned_data
        form.save()
        form = SportForm()
        messages.success(request, 'post done successfully')

    context = {
        'form': form
    }

    return render(request, 'html/publish.html', context)


def podelete(request, id):
    post = Statistic.objects.get(id=id)
    post.delete()
    return redirect('info')


def edit_post(request, id):
    single_post = get_object_or_404(Statistic,pk=id)
    form = SportForm(request.POST or None, instance=single_post)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }
    return render(request, 'html/edit.html', context)

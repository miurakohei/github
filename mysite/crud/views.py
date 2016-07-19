from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm

def index(request):
    d={
        'messages':Message.objects.all(),
    }
    return render(request,'crud/index.html',d)

def add(request):
    return render(request,'crud/edit.html',{})

def edit(request, editing_id):
    return render(request, 'crud/edit.html',{})

def delete(request):
    return HttpResponse('Delete')

def add(request):
    form=MessageForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('crud:index')

    d={
        'form':form,
    }
    return render(request,'crud/edit.html',d)

def edit(request,editing_id):
    message=get_object_or_404(Message,id=editing_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message.message=form.cleaned_data['message']
            message.save()
            return redirect('crud:index')
    else:
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        form=MessageForm({'message':message.message})
    d={
        'form':form,
    }
    return render(request,'crud/edit.html',d)

def delete(request):
    delete_ids=request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('crud:index')

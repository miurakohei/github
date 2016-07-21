from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import User
from cms.forms import UserForm


def user_list(request):
    """顧客一覧"""
    # return HttpResponse('顧客の一覧')
    users=User.objects.all().order_by('id')
    return render(request,
                  'cms/user_list.html',
                  {'users':users})


def user_edit(request, user_id=None):
    """顧客の編集"""
    # return HttpResponse('顧客の編集')
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user=User()

    if request.method == 'POST':
        form=UserForm(request.POST, instance=user)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('cms:user_list')
    else:
        form=UserForm(instance=user)

    return render(request, 'cms/user_edit.html', dict(form=form, user_id=user_id))

def user_del(request, user_id):
    """顧客の削除"""
    # return HttpResponse('顧客の削除')
    user=get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('cms:user_list')

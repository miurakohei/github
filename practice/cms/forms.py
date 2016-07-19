from django.forms import ModelForm
from cms.models import User


class UserForm(ModelForm):
    """顧客のフォーム"""
    class Meta:
        model = User
        fields=('name','post','address')
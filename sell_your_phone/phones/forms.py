from django import forms

from sell_your_phone.core.forms import BootstrapFormMixin
from sell_your_phone.phones.models import Phone
from sell_your_phone.phones.models import Comment


class SellPhoneForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ('user',)


class EditPhoneForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ('user',)
        widgets = {
            'brand': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class SearchForm(forms.Form):
    q = forms.CharField(label='Search by brand OR model', max_length=30)

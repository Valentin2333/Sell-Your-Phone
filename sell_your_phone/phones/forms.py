from django import forms

from sell_your_phone.core.forms import BootstrapFormMixin
from sell_your_phone.phones.models import Phone
from sell_your_phone.phones.models import Comment
import os
from os.path import join
from sell_your_phone import settings


class SellPhoneForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ('user',)


class EditPhoneForm(BootstrapFormMixin, forms.ModelForm):
    #def save(self, commit=True):
    #    db_phone = P#hone.objects.get(pk=self.instance.id)
    #    if commit:
    #        image_path = join(settings.MEDIA_ROOT, str(db_phone.image))
    #        os.remove(image_path)
    #    return super().save(commit)

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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from sell_your_phone.phones.forms import SellPhoneForm, CommentForm, EditPhoneForm
from sell_your_phone.phones.models import Phone, Comment, Like


class ListPhonesView(ListView):
    template_name = 'phones/phone_list.html'
    context_object_name = 'phones'
    model = Phone


def phone_details(request, pk):
    phone = Phone.objects.get(pk=pk)
    phone.likes_count = phone.like_set.count()
    is_owner = phone.user == request.user
    is_liked_by_user = phone.like_set.filter(user_id=request.user.id).exists()
    context = {
        'phone': phone,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk
            }
        ),
        'comments': phone.comment_set.all(),
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
    }
    return render(request, 'phones/phone_details.html', context=context)


@login_required
def comment_phone(request, pk):
    phone = Phone.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['text'],
            phone=phone,
            user=request.user,
        )
        comment.save()

    return redirect('phone details', pk)


@login_required
def like_phone(request, pk):
    phone = Phone.objects.get(pk=pk)
    object_liked_by_user = phone.like_set.filter(user_id=request.user.id).first()
    if object_liked_by_user:
        object_liked_by_user.delete()
    else:
        like = Like(phone=phone, user=request.user)
        like.save()
    return redirect('phone details', phone.id)


class SellPhoneView(LoginRequiredMixin, CreateView):
    model = Phone
    form_class = SellPhoneForm
    success_url = reverse_lazy('list phones')
    template_name = 'phones/phone_sell.html'

    def form_valid(self, form):
        phone = form.save(commit=False)
        phone.user = self.request.user
        phone.save()
        return super().form_valid(form)


class EditPhoneView(LoginRequiredMixin, UpdateView):
    model = Phone
    form_class = EditPhoneForm
    success_url = reverse_lazy('list phones')
    template_name = 'phones/phone_edit.html'


class DeletePhoneView(LoginRequiredMixin, DeleteView):
    model = Phone
    success_url = reverse_lazy('list phones')
    template_name = 'phones/phone_delete.html'
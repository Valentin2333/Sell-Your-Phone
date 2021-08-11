from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from sell_your_phone.accounts.forms import LoginForm, RegisterForm, ProfileForm
from sell_your_phone.phones.models import Phone
from sell_your_phone.accounts.models import Profile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def profile_details(request):
    profile = Profile.objects.filter(user_id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm()

    user_phones = Phone.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'phones': user_phones,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)

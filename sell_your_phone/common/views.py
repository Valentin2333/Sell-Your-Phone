from django.views.generic import TemplateView

from sell_your_phone.phones.forms import SearchForm


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context

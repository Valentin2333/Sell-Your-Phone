from django.views.generic import TemplateView, FormView

from sell_your_phone.phones.forms import SearchForm


class Index(TemplateView, FormView):
    template_name = 'index.html'
    form_class = SearchForm


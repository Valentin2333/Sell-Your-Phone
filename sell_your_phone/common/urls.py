from django.urls import path
from sell_your_phone.common.views import Index


urlpatterns = [
    path('', Index.as_view(), name='index'),
]

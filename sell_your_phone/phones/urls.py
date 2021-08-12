from django.urls import path

from sell_your_phone.phones.views import ListPhonesView, phone_details, comment_phone, like_phone, SellPhoneView, \
    EditPhoneView, DeletePhoneView, SearchResultsView

urlpatterns = [
    path('', ListPhonesView.as_view(), name='list phones'),
    path('details/<int:pk>', phone_details, name='phone details'),
    path('comment/<int:pk>', comment_phone, name='comment phone'),
    path('like/<int:pk>', like_phone, name='like phone'),
    path('sell/', SellPhoneView.as_view(), name='sell phone'),
    path('edit/<int:pk>', EditPhoneView.as_view(), name='edit phone'),
    path('delete/<int:pk>', DeletePhoneView.as_view(), name='delete phone'),
    path('search/', SearchResultsView.as_view(), name='search results'),
]

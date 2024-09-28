from django.urls import path
from .views import UniversitetListView, TalabaListView, BinoListView

urlpatterns = [
    path('', UniversitetListView.as_view(), name='home'),  # Asosiy sahifa sifatida universitetlar ro'yxati
    path('universitetlar/', UniversitetListView.as_view(), name='universitet_list'),
    path('talabalar/', TalabaListView.as_view(), name='talaba_list'),
    path('binolar/', BinoListView.as_view(), name='bino_list'),
]

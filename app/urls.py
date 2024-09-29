from django.urls import path
from .views import UniversitetListView, BinoListView

urlpatterns = [
    path('', UniversitetListView.as_view(), name='home'),  # Asosiy sahifa sifatida universitetlar ro'yxati
    path('universitetlar/', UniversitetListView.as_view(), name='universitet_list'),
    path('binolar/', BinoListView.as_view(), name='bino_list'),
]

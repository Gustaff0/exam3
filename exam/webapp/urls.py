from django.urls import path
from webapp.views import ProductCreate, ProductList, ProductEdit, ProductView, ProductDelete

app_name = 'webapp'

urlpatterns = [
    path('create/', ProductCreate.as_view(), name='create'),
    path('', ProductList.as_view(), name='home'),
    path('edit/<int:pk>/', ProductEdit.as_view(), name='edit'),
    path('view/<int:pk>/', ProductView.as_view(), name='view'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete')
]
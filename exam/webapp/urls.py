from django.urls import path
from webapp.views import ProductCreate, ProductList, ProductEdit, ProductView, ProductDelete, FeedbackCreate, FeedbackEdit, FeedbackDelete, FeedbackModerList, FeedBackChekModer

app_name = 'webapp'

urlpatterns = [
    path('create/', ProductCreate.as_view(), name='create'),
    path('', ProductList.as_view(), name='home'),
    path('edit/<int:pk>/', ProductEdit.as_view(), name='edit'),
    path('view/<int:pk>/', ProductView.as_view(), name='view'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
    path('add/feedback/<int:pk>/', FeedbackCreate.as_view(), name='create_feedback'),
    path('delete/feedback/<int:pk>/', FeedbackDelete.as_view(), name='delete_feedback'),
    path('edit/feedback/<int:pk>/', FeedbackEdit.as_view(), name='edit_feedback'),
    path('edit/checkmoder/<int:pk>/', FeedBackChekModer.as_view(), name='edit_check_moder'),
    path('edit/checkmoder/', FeedbackModerList.as_view(), name='list_check_moder')
]
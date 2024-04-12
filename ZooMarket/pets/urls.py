from django.urls import path, re_path
import pets.views as pets

urlpatterns = [
    path('', pets.index, name='main_url'),
    # path('petGet/', pets.petGet),
    path('feedback/', pets.feedback),
    path('edit_feedback/<int:feedback_id>/', pets.edit_feedback),
    path('delete_feedback/<int:feedback_id>/', pets.delete_feedback),
    path('<slug:slug_pets>/', pets.info_pets),
    path('cats/<int:category_id>/', pets.categories),
]


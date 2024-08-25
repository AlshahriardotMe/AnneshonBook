from django.urls import path
from booklist import views

urlpatterns = [
    path('Book_List_cmt/', views.Book_List_cmt, name='Book_List_cmt'),
    path('Book_List_et/', views.Book_List_et, name='Book_List_et'),
    path('Book_List_ent/', views.Book_List_ent, name='Book_List_ent'),
    path('Book_List_ct/', views.Book_List_ent, name='Book_List_ct'),
    path('Book_List_mac/', views.Book_List_ent, name='Book_List_mac'),
    path('Book_List_ft/', views.Book_List_ent, name='Book_List_ft'),
   
]
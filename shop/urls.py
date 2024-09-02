from django.urls import path
from shop import views

urlpatterns = [
    path('',views.home, name='home'),
    path('Free_book/',views.Free_book, name='Free_book'), 
    path('Contact/',views.Contact, name='Contact'), 
    path('Product_details/',views.Product_details, name='Product_details'), 
    path('Profile/',views.Profile, name='Profile'), 
    path('AddToCart/',views.AddToCart, name='AddToCart'), 
    
    path('All_books/',views.All_books, name='All_books'), 
    path('Login/',views.Login, name='Login'), 
    path('Registration/',views.Registration, name='Registration'), 
    
    path('Cmt_all/',views.Cmt_all, name='Cmt_all'), 
    path('Cmt_First_semeter/',views.Cmt_First_semeter, name='Cmt_First_semeter'), 
    path('Cmt_Second_semeter/',views.Cmt_Second_semeter, name='Cmt_Second_semeter'), 
    path('Cmt_Third_semeter/',views.Cmt_Third_semeter, name='Cmt_Third_semeter'), 
    path('Cmt_Fourth_semeter/',views.Cmt_Fourth_semeter, name='Cmt_Fourth_semeter'), 
    path('Cmt_Fifth_semeter/',views.Cmt_Fifth_semeter, name='Cmt_Fifth_semeter'), 
    path('Cmt_Sixth_semeter/',views.Cmt_Sixth_semeter, name='Cmt_Sixth_semeter'), 
    path('Cmt_Seventh_semeter/',views.Cmt_Seventh_semeter, name='Cmt_Seventh_semeter'), 
]
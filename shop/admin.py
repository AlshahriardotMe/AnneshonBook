from django.contrib import admin
from .models import  Writer, Book, Review
# Register your models here.


    
    
@admin.register(Writer)
class WriterModelAdmin(admin.ModelAdmin):
    list_display=['id','name','institution', 'bio','pic','updated_at']
    
@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title','writer','subject','semester','regulations','subjectcode','publication_date','price','description','cover_image','pdf_file','stock']
    
    
@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display=['id','customer','book','review_star','review_text','created']
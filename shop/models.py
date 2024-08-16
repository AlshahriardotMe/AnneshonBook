from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.name
  
class Subcategory(models.Model):
	name = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.name
  


class Writer(models.Model):
	name = models.CharField(max_length = 100)
	bio = models.TextField()
	pic = models.FileField(upload_to = "writer/")
	updated_at = models.DateTimeField(auto_now_add = True)
    
	def __str__(self):
		return self.name




class Book(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    subject = models.ForeignKey(Category, on_delete = models.CASCADE)
    semester = models.ForeignKey(Subcategory, on_delete = models.CASCADE)
    regulations = models.CharField(max_length=100)
    subjectcode = models.CharField(max_length=10)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers', blank=True,null=True)
    pdf_file = models.FileField(upload_to='book_pdfs', blank=True, null=True)
    totalreview = models.IntegerField(default=1)
    totalrating = models.IntegerField(default=5)

    def __str__(self):
       return self.title

class Review(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_star = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

    

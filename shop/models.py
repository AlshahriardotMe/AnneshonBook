from django.db import models
from django.contrib.auth.models import User


  


class Writer(models.Model):
	name = models.CharField(max_length = 100)
	institution = models.CharField(max_length=100)
	bio = models.TextField()
	pic = models.FileField(upload_to = "writer/")
	updated_at = models.DateTimeField(auto_now_add = True)
    
	def __str__(self):
		return self.name

SUBJECT_CHOOSE =(
	('','Choose Your subject'),
	('CMT','Computer'),
	('CE','Civil '),
	('ET','Electrical'),
	('ENT','Electronics'),
	('ME','Mechanical'),
	('FT','Food'),
	('RAC','RAC'),
	('MCT','Mechatronics'),
	
)

SENESTER_CHOOSE =(
	('','Choose Your semerter'),
	('FS','First'),
	('SD','Second'),
	('TH','Third'),
	('FR','Fourth'),
	('FI','Fifth'),
	('SI','Sixth'),
	('SE','Seventh')
	
)

REGULATION_CHOOSE = (
	('','Choose Your semerter'),
	('16','2016'),
	('22','2022'),
)




class Book(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    subject = models.CharField(choices=SUBJECT_CHOOSE, max_length=100)
    semester = models.CharField(choices=SENESTER_CHOOSE, max_length=20)
    regulations = models.CharField(choices=REGULATION_CHOOSE , max_length=20)
    subjectcode = models.CharField(max_length=10)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers', blank=True,null=True)
    pdf_file = models.FileField(upload_to='book_pdfs', blank=True, null=True)
    stock = models.IntegerField()

    def __str__(self):
       return self.title

class Review(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_star = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

    

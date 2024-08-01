from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DIVISION_CHOICES = (
    ('','Choose Your Divicion'),
    ('Dhaka', 'Dhaka'),
    ('Khulna', 'Khulna'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Rajshahi', 'Rajshahi'),
    ('Barishal', 'Barishal'),
    ('Chattogram', 'Chattogram'),
    ('Mymendhing', 'Mymendhing'),
) 
  

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    name = models.CharField(max_length=150),
    institution = models.CharField(max_length=150),
    division = models.CharField(choices=DIVISION_CHOICES ,max_length=50),
    district = models.CharField(max_length=50),
    Thana = models.CharField(max_length=50),
    zipcode = models.IntegerField(),
    image = models.ImageField(),
    
    
    def __str__(self):
        return str(self.id)
    
from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    subjectcode = models.CharField(max_length=10)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers', blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    pdf_file = models.FileField(upload_to='book_pdfs', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.book}"

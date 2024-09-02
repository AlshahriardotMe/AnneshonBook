from django.shortcuts import render 

# Create your views here.
def home(request):
    return render(request, 'shop/home.html')

# ,,,,,,,Free book ,,,,,,,,,,,,,,,,,
def Free_book(request):
    return render(request, 'shop/free-book.html')
# ,,,,,,,Free book ,,,,,,,,,,,,,,,,,
def Contact(request):
    return render(request, 'shop/contact.html')

# ------------------Add to Carts --------------------------------

def AddToCart(request):
    return render(request, 'shop/add-to-cart.html')

def All_books(request):
    return render(request, 'shop/all-books.html')

# ----------- product Details --------
def Product_details(request):
    return render(request, 'shop/product_details.html')


# ----------------------profile -------------------->

def Profile(request):
    return render(request, 'shop/profile.html')


# ----------------------login -------------------->
def Login(request):
    return render(request, 'shop/login.html')

# ----------------------Registration -------------------->
def Registration(request):
    return render(request, 'shop/registration.html')

#-------------------------COMPUTER OF semesterS ---->
def Cmt_all(request):
    return render(request, 'cmt/cmt-all.html')

def Cmt_First_semeter(request):
    return render(request, 'cmt/semester-one.html')

def Cmt_Second_semeter(request):
    return render(request, 'cmt/semester-two.html')

def Cmt_Third_semeter(request):
    return render(request, 'cmt/semester-three.html')

def Cmt_Fourth_semeter(request):
    return render(request, 'cmt/semester-fore.html')

def Cmt_Fifth_semeter(request):
    return render(request, 'cmt/semester-five.html')

def Cmt_Sixth_semeter(request):
    return render(request, 'cmt/semester-six.html')

def Cmt_Seventh_semeter(request):
    return render(request, 'cmt/semester-seven.html')


#-------------------------ET OF semesterS ---->


def Et_First_semeter(request):
    return render(request, 'shop/home.html')

def Et_Second_semeter(request):
    return render(request, 'shop/home.html')

def Et_Third_semeter(request):
    return render(request, 'shop/home.html')

def Et_Fourth_semeter(request):
    return render(request, 'shop/home.html')

def Et_Fifth_semeter(request):
    return render(request, 'shop/home.html')

def Et_Sixth_semeter(request):
    return render(request, 'shop/home.html')

def Et_Seventh_semeter(request):
    return render(request, 'shop/home.html')



#-------------------------ENT OF semesterS ---->


def Ent_First_semeter(request):
    return render(request, 'shop/home.html')

def Ent_Second_semeter(request):
    return render(request, 'shop/home.html')

def Ent_Third_semeter(request):
    return render(request, 'shop/home.html')

def Ent_Fourth_semeter(request):
    return render(request, 'shop/home.html')

def Ent_Fifth_semeter(request):
    return render(request, 'shop/home.html')

def Ent_Sixth_semeter(request):
    return render(request, 'shop/home.html')

def Ent_Seventh_semeter(request):
    return render(request, 'shop/home.html')


#-------------------------FOOT OF semester---->


def Ft_First_semeter(request):
    return render(request, 'shop/home.html')

def Ft_Second_semeter(request):
    return render(request, 'shop/home.html')

def Ft_Third_semeter(request):
    return render(request, 'shop/home.html')

def Ft_Fourth_semeter(request):
    return render(request, 'shop/home.html')

def Ft_Fifth_semeter(request):
    return render(request, 'shop/home.html')

def Ft_Sixth_semeter(request):
    return render(request, 'shop/home.html')

def Ft_Seventh_semeter(request):
    return render(request, 'shop/home.html')


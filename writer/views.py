from django.shortcuts import render

# Create your views here.
def writer(request):
    return render(request, 'shop/writer.html')
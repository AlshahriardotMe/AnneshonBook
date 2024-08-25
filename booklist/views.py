from django.shortcuts import render

# Create your views here.
# -------------------Book List ----------------
def Book_List_cmt(request):
    return render(request, 'booklist/cmt.html')
def Book_List_et(request):
    return render(request, 'booklist/et.html')
def Book_List_ent(request):
    return render(request, 'booklist/ent.html')

def Book_List_ct(request):
    return render(request, 'booklist/ct.html')
def Book_List_mac(request):
    return render(request, 'booklist/mac.html')
def Book_List_ft(request):
    return render(request, 'booklist/ft.html')
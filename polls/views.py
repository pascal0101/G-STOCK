from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
    

def vente(request):
    ventes = Vente.objects.all()
    categories = Categorie.objects.all()
    if request.method == 'POST':
        produit_id = request.POST.get('produit')
        quantite = request.POST.get('quantite')
        #produit=(get_object_or_404(Produit, pk=produit_id)).id
        #print(produit)
        p_id = Produit.objects.get(pk=produit_id)
        c = Vente(produit=p_id,quantite=quantite)
        print(p_id)
        c.save()
        print("form is ok")
        
    return render(request,'vente.html',{'ventes':ventes, 'categories':categories})


def rapport(request):
    return render(request,'rapport.html')

from django.shortcuts import render
from .models import Medicine, Supplier, Supply

def index(request):
    medicines = Medicine.objects.all()
    suppliers = Supplier.objects.all()
    supplies = Supply.objects.all()
    return render(request, 'pharmacy/index.html', {
        'medicines': medicines,
        'suppliers': suppliers,
        'supplies': supplies,
    })

from django.shortcuts import render
from.forms import ProductForm,DeletingData,UpdatingData
from django.http.response import HttpResponse
from.models import ProductData
def main_page(request):
    return render(request,'main_page.html')
def inserting_view(request):
    if request.method == "POST":
        pform=ProductForm(request.POST)
        if pform.is_valid():
            product_number = request.POST.get('product_number','')
            product_name = request.POST.get('product_name','')
            product_cost = request.POST.get('product_cost','')
            product_class = request.POST.get('product_class','')
            product_weight= request.POST.get('product_weight','')
            data=ProductData(
                product_number=product_number,
                product_name=product_name,
                product_cost=product_cost,
                product_class=product_class,
                product_weight=product_weight,

            )
            data.save()
            pform = ProductForm()
            return render(request,'insertingdata.html',{'pform':pform})
    else:
        pform=ProductForm()
        return render(request,'insertingdata.html',{'pform':pform})

def retrieving_view(request):
    data=ProductData.objects.all()
    return render(request,'retrieving.html',{'data':data})
def update_view(request):
    if request.method=='POST':
        uform = UpdatingData(request.POST)
        if uform.is_valid():
            product_number = request.POST.get('product_number','')
            product_cost = request.POST.get('product_cost','')
            pnum = ProductData.objects.filter(product_number=product_number)
            if not pnum:
                return HttpResponse("product not available")
            else:
                pnum.update(product_cost=product_cost)
                uform = UpdatingData()
                return render(request, 'update.html', {'uform': uform})




    else:
        uform=UpdatingData()
        return render(request,'update.html',{'uform':uform})
def delete_view(request):
    if request.method == "POST":
        dform=DeletingData(request.POST)
        if dform.is_valid():
            product_number = request.POST.get('product_number','')
            pnum = ProductData.objects.filter(product_number=product_number)
            if not pnum:
                return HttpResponse("invalid product number")
            else:
                pnum.delete()
                dform = DeletingData()
                return render(request, 'deleting.html', {'dform': dform})

    else:
        dform=DeletingData()
        return render(request,'deleting.html',{'dform':dform})

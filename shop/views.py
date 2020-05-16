from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact,Orders,orderUpdate
from math import ceil
import json
# Create your views here.
def index (request):
    #products=Products.objects.all()
    #print(products)
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])
    #allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    # params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    params ={'allprods':allprods}
    return render(request, 'shop/index.html',params)
    #return HttpResponse("Hello Infinity")

def searchMatch(query, item):
    #return true only if query matches the item
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False



def search(request):
    #this is gonna take that element from that serch box and in using prod show it out
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        #serchMatch is a fxn that is gonna return true if it is find it
        prod = [item for item in prodtemp if searchMatch(query , item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        #we are using it here to stop showing some unknown buttons which our website is showing if the products are not present
        if len(prod) != 0:
            allprods.append([prod, range(1, nslides), nslides])
    # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    # params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    params = {'allprods': allprods,"msg":""}
    #if try to search empty search so for that
    if len(allprods) == 0 or len(query)<4:
        params = {'msg':"Please Make Sure To Enter Relevant Search Query"}
    return render(request, 'shop/search.html', params)
    # return HttpResponse("Hello Infinity")




def about (request):
    return render(request, 'shop/about.html')



def contact(request):
    thank = False
    if request.method=="POST":
        name =request.POST.get('name','')
        email =request.POST.get('email','')
        phone =request.POST.get('phone','')
        desc =request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html',{'thank' : thank})
def tracker(request):
    if request.method=="POST":
        orderId =request.POST.get('orderId','')
        email =request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if(len(order)>0):
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.appen({'text': item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')






def prodview(request,myid):
    #Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodview.html',{'product':product[0]})



def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address=request.POST.get('address', '') + " " + request.POST.get('address2', '')
        #address2 = request.POST.get('email', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json,name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The Order Has Been Placed")
        update.save()
        thank =True
        id=order.order_id
        return render(request, 'shop/checkout.html',{'thank':thank,'id': id})
    return render(request, 'shop/checkout.html')

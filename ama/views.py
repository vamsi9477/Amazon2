from django.shortcuts import render
from .models import amazonwebsite
from .models import paymentprocesses
from .models import comments
# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def HeadSection(request):
    return render(request,"head.html")


def BodySection(request):
    return render(request,"body.html")


def Register(request):
    return render(request,"registration.html")

def Registration(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t3")
    username=request.POST.get("t4")
    password=request.POST.get("t5")
    address=request.POST.get("t6")
    a=amazonwebsite(name=name,cno=cno,email=email,username=username,password=password,address=address)
    a.save()
    return render(request,"productdetails.html",{"emp":"Details Saved in Sqlite 3 Database"})

def Login(request):
    return render(request,"login.html")


def accountexist(request):
    return render(request,"accountalreadyexist.html")

def AccountalreadyExist(request):
    return render(request,"productdetails.html")


def ProductDetails(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    user=amazonwebsite.objects.filter(username=username,password=password)
    if not user:
        return render(request,"accountalreadyexist.html")
    else:
        return render(request,"productdetails.html")


def AboutUs(request):
    return render(request,"about us.html")


def ContactUs(request):
    return render(request,"contactwithus.html")


def HomePage(request):
    return render(request,"homepage.html")


def wikipedia(request):
    return render(request,"wikipedia.html")



def purchase(request):
    return render(request,"proceed.html")

def purchaseItem(request):
    watchestypes=request.POST.get("WatchesTypes")
    watchesname=request.POST.get("Watches Names")
    Money=request.POST.get("Money")
    customercno=request.POST.get("t1")
    customeradd=request.POST.get("t2")
    cardtype=request.POST.get("Customer Card Type")
    bankname=request.POST.get("Bank Name")
    cardnumber=request.POST.get("t3")
    cardname=request.POST.get("t4")
    cvvno=request.POST.get("t5")
    pp=paymentprocesses(watchestypes=watchestypes,watchesname=watchesname,Money=Money,customercno=customercno,customeradd= customeradd,
                        cardtype=cardtype,bankname=bankname,cardnumber=cardnumber,cardname=cardname,cvvno=cvvno)
    pp.save()
    return render(request,"proceed.html",{"purchaseitem":"Your Delivery will be Delivered Soon."})


def Addcart(request):
    return render(request,"addcart.html")


def Logout(request):
    return render(request,"body.html")

def Comments(request):
    return render(request,"comments.html")

def CommentsSection(request):
    comment=request.POST.get("comments")
    c=comments(comment=comment)
    c.save()
    return render(request,"comments.html")


def Adminstration(request):
    return render(request,"adminstration.html")


def AdminstrationDetails(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    if username=="admin"  and password=="admin":
        return render(request,"adminproductview.html")
    else:
        return render(request,"adminstration.html")

def viewProduct(request):
    return render(request,"productviewdetails.html")


def viewProductDetails(request):
    pp1=paymentprocesses.objects.all()
    print(pp1)
    return render(request,"productviewdetails.html",{"key":pp1})


def viewPurchase(request):
    return render(request,"viewpurchasedetails.html")


def viewPurchaseDetails(request):
    pp = paymentprocesses.objects.all()
    print(pp)
    return render(request,"viewpurchasedetails.html",{"key1":pp})


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth import authenticate, login
from laptop.models import Customer, Technician
from laptop.models import Laptop, Requests
import datetime

def index(request):
    laptops=Laptop.objects.all()[0:3]

    return render(request, 'core/index.html',
                  {'laptops':laptops, 
                   })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #phone_number = request.POST['phone_number']
        if password == confirm_password:
            customer_count = Customer.objects.count()
            new_customer_id = f"C{customer_count + 1}"
            customer = Customer(name=name, emailid=emailid,password=password,custid=new_customer_id)
            customer.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            error_message = "Passwords don't match"
            return render(request, 'core/signup.html', {'error_message': error_message})
    else:
        return render(request, 'core/signup.html')
    
def admin_add_laptop(request):
    if request.method == 'POST':
        #prodid = request.POST['prodid']
        brand_name = request.POST['brand_name']
        model_name = request.POST['model_name']
        price = request.POST['price']
        date_of_manf = request.POST['date_of_manf']
        processor = request.POST['processor']
        if 'ram' in request.POST:
            ram = request.POST['ram']
        else:
            ram = ''
        ram = request.POST.get('ram', '')
        size = request.POST['size']
        screen_type = request.POST['screen_type']
        OpSys = request.POST['OS']
        Storage = request.POST['Storage']
        laptop_count = Laptop.objects.count()
        new_laptop_id = f"L{laptop_count + 1}"
        new_laptop = Laptop(prodid=new_laptop_id, brand_name=brand_name, model_name=model_name, price=price, date_of_manf=date_of_manf,
                            processor=processor, ram=ram, size=size, screen_type=screen_type, OS=OpSys, Storage=Storage)
        new_laptop.save()
        return HttpResponseRedirect(reverse('admin_home'))
    else:
        return render(request, 'core/admin_add_laptop.html')

def admin_add_technician(request):
    if request.method == 'POST':
        #techid = request.POST['techid']
        tname = request.POST['tname']
        tusername = request.POST['tusername']
        hiredate = request.POST['hiredate']
        password = request.POST['password']
        salary = request.POST['salary']
        technician_count = Technician.objects.count()
        new_technician_id = f"T{technician_count + 1}"
        technician = Technician( tname=tname, tusername=tusername, hiredate=hiredate, password=password, salary=salary, techid=new_technician_id)
        technician.save()
        return HttpResponseRedirect(reverse('admin_home'))
    else:
        return render(request, 'core/admin_add_technician.html')

def user_repair(request):
    if request.method == 'POST':
        #reqid = request.POST['reqid']
        #custid = request.POST['custid']
        repair_type = request.POST['repair_type']
        user_desc = request.POST['user_desc']
        request_count = Requests.objects.count()
        date_of_req = datetime.date.today()
        new_request_id = f"RR{request_count + 1}"
        request = Requests(reqid=new_request_id,date_of_req=date_of_req,repair_type=repair_type,user_desc=user_desc)
        request.save()
        #create_request(reqid, custid, date_of_req, repair_type, user_desc)
        return HttpResponseRedirect(reverse('user_home'))
    else:
        return render(request, 'core/user_repair.html')

'''def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        #user = authenticate(request, email=email, password=password)
        #validcustomer=Customer.objects.filter(emailid=email,password=password)
        if Customer.emailid!=email and Customer.password!=password:
            #login(request, validcustomer)
            #return HttpResponseRedirect(reverse('index'))
            return render(request, 'core/index.html')
        else:
            error_message = "Invalid email or password"
            return render(request, 'core/login.html', {'error_message': error_message})
    else:
        return render(request, 'core/login.html')'''

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email=="daanishshaikh24ap@gmail.com" and password=="Daanish@123":
            return render(request, 'core/admin_home.html')
        try:
            customer = Customer.objects.get(emailid=email)
            if customer.password == password:
                #login(request, customer)
                return render(request, 'core/user_home.html')
            else:
                messages.error(request, 'Invalid email or password')
                return render(request, 'core/login.html')
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')
    
def admin_all_technicians(request):
    with connection.cursor() as cursor:
        cursor.callproc('display_technician_table')
        technicians = cursor.fetchall()
    return render(request, 'core/admin_all_technicians.html', {'technicians': technicians})

def user_home(request):
    return render(request, 'core/user_home.html')

def admin_home(request):
    return render(request, 'core/admin_home.html')

def admin_receipts(request):
    return render(request, 'core/admin_receipts.html')

def admin_laptops(request):
    return render(request, 'core/admin_laptops.html')

def admin_employees(request):
    return render(request, 'core/admin_employees.html')

def user_buy(request):
    with connection.cursor() as cursor:
        cursor.callproc('display_laptop_table')
        laptops = cursor.fetchall()
    return render(request, 'core/user_buy.html', {'laptops': laptops})

#def user_repair(request):
#    return render(request, 'core/user_repair.html')

def laptop_list(request):
    with connection.cursor() as cursor:
        cursor.callproc('display_laptop_table')
        laptops = cursor.fetchall()
    return render(request, 'core/laptop_list.html', {'laptops': laptops})

'''@receiver(post_save, sender=Laptop)
def log_laptop_changes(sender, instance, created, **kwargs):
    laptop = Laptop.objects.get()
    action = 'insert' if created else 'update'
    LaptopLog.objects.create(
        action=action,
        prodid=laptop.prodid,
        brand_name=laptop.brand_name,
        model_name=laptop.model_name,
        price=laptop.price,
        date_of_manf=laptop.date_of_manf,
        processor=laptop.processor,
        ram=laptop.ram,
        size=laptop.size,
        screen_type=laptop.screen_type,
        OS=laptop.OS,
        Storage=laptop.Storage
    )'''
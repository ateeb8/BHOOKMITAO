from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from datetime import date

# Create your views here.
def index(request):
      return render(request,'index.html')
def all_logins(request):
      return render(request,'all_logins.html')


def read_more(request):
    return render(request, 'read_more.html')

def donor_login(request):
      if request.method == "POST":
         u = request.POST['emailid']
         p = request.POST['pwd']
         user = authenticate(username=u,password=p)
         if user:
             login(request,user)
             error = "no"
         else:
             error = "yes"
      return render(request,'donor_login.html',locals())

def donor_reg(request):
      error = ""
      if request.method == "POST":
            fn = request.POST['firstname']
            ln = request.POST['lastname']
            em = request.POST['email']
            contact = request.POST['contact']
            pwd = request.POST['pwd']
            userpic = request.FILES['userpic']
            address = request.POST['address']

            try:
                user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
                Donor.objects.create(user=user,contact=contact,userpic=userpic, address=address)
                error = "no"
            except:
                error = "yes"


      return render(request,'donor_reg.html',locals()) #error is a local variable


def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    total_donations = donation.count()
    accept_donations = donation.filter(status='accept').count()
    reject_donations = donation.filter(status='reject').count()
    pending_donations = donation.filter(status='pending').count()
    rev_donations = donation.filter(status='Donation Received').count()
    delivered_donations = donation.filter(status='Donation Delivered').count()

    context={
        'user':user,
        'donor':donor,
        'donation':donation,
        'total_donations':total_donations,
        'accept_donations':accept_donations,
        'reject_donations': reject_donations,
        'pending_donations': pending_donations,
        'rev_donations': rev_donations,
        'delivered_donations': delivered_donations,

    }
    return render(request, 'donor_home.html', context)



def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method=="POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        quantity = request.POST['quantity']
        quality = request.POST['quality']
        collectionloc = request.POST['collectionloc']
        pinlocation = request.POST['pinlocation']
        description = request.POST['description']
        try:
            Donation.objects.create(donor=donor,donationname=donationname,donationpic=donationpic,quantity=quantity,quality=quality,collectionloc=collectionloc,pinlocation=pinlocation,description=description,status="pending")
            error="no" #we use create when we have to enter data in database
        except:
            error="yes"


    return render(request, 'donate_now.html',locals())

def Logout(request):
    logout(request) #it expires the data and redirect to index
    return redirect('index')

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor) #filter is use for fetching all data
    return render(request, 'donation_history.html',locals())

def view_donationdetail(request,pid): #the view details show trough id
    if not request.user.is_authenticated:
        return redirect('donor_login')
    donation = Donation.objects.get(id=pid) #get is use for fetching a single data
    return render(request, 'view_donationdetail.html',locals())

def edit_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')

    donation = Donation.objects.get(id=pid)
    if request.method=="POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        quantity = request.POST['quantity']
        quality = request.POST['quality']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        donation.donationname = donationname
        donation.donationpic = donationpic
        donation.quantity = quantity
        donation.quality = quality
        donation.collectionloc = collectionloc
        donation.description = description
        try:
            donation.save()
            error="no"
        except:
            error="yes"



    return render(request, 'edit_donationdetail.html',locals())

def delete_donationdetail(request,pid):
    donation= Donation.objects.get(id=pid).delete()
    return redirect('donation_history')


def admin_login(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
           if user.is_staff:
              login(request, user)
              error = "no"
           else:
              error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html',locals())


def volunteer_login(request):
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
          try:
             user1 = Volunteer.objects.get(user=user)
             if user1.status != "pending":
                 login(request, user)
                 error = "no"
             else:
                error = "not"
          except:
            error = "yes"

    else:
        error = "yes"
    return render(request, 'volunteer_login.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.all()
    donation = Donation.objects.all()
    donor = Donor.objects.all()
    total_donors= donor.count()
    total_donations=donation.count()
    all_volunteer = volunteer.count()
    new_donations = donation.filter(status='pending').count()
    new_volunteers = volunteer.filter(status='pending').count()

    context = {
        'volunteer':volunteer,
        'donation':donation,
        'all_volunteer':all_volunteer,
        'total_donations':total_donations,
        'new_donations': new_donations,
        'total_donors':total_donors,
        'new_volunteers':new_volunteers
    }

    return render(request, 'admin_home.html',context)

def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="pending") #filter is use for fetching all data
    return render(request, 'pending_donation.html',locals())

def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="accept") #filter is use for fetching all data
    return render(request, 'accepted_donation.html',locals())


def admin_view_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']

        try:
            donation.adminremark = adminremark
            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'admin_view_donationdetail.html',locals())

def add_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if request.method=="POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        try:
            DonationArea.objects.create(areaname=areaname,description=description)
            error="no" #we use create when we have to enter data in database
        except:
            error="yes"


    return render(request, 'add_area.html',locals())

def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = DonationArea.objects.all()
    return render(request, 'manage_area.html',locals())

def edit_area(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = DonationArea.objects.get(id=pid)
    if request.method=="POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        area.areaname = areaname
        area.description = description
        try:
            area.save()
            error="no" #we use create when we have to enter data in database
        except:
            error="yes"


    return render(request, 'edit_area.html',locals())

def view_area(request,pid): #the view details show trough id
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = DonationArea.objects.get(id=pid) #get is use for fetching a single data
    return render(request, 'view_area.html',locals())

def delete_area (request,pid):
    DonationArea.objects.get(id=pid).delete()
    return redirect('manage_area')

def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.all()
    return render(request, 'manage_donor.html',locals())

def view_donordetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)
    return render(request, 'view_donordetail.html',locals())

def delete_donor (request,pid):
    User.objects.get(id=pid).delete()
    return redirect('manage_donor')

def delete_volunteer (request,pid):
    User.objects.get(id=pid).delete()
    return redirect('all_volunteer')



def volunteer_registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        address = request.POST['address']
        aboutme = request.POST['aboutme']



    try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic,  address=address, aboutme=aboutme,  status="pending")
            error = "no"
    except:
            error = "yes"

    return render(request, 'volunteer_registration.html', locals())  # error is a local variable


def volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer)
    total_donations = donation.count()
    new_donations = donation.filter(status='Volunteer Allocated').count()
    delivered_donations = donation.filter(status='Donation Delivered').count()

    context={
        'user':user,
        'volunteer':volunteer,
        'donation':donation,
        'total_donations':total_donations,
        'new_donations':new_donations,
        'delivered_donations':delivered_donations,
    }
    return render(request, 'volunteer_home.html',context)


def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="pending")
    return render(request, 'new_volunteer.html',locals())


def view_volunteerdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']

        try:
            volunteer.adminremark = adminremark
            volunteer.status = status
            volunteer.updationdate = date.today()
            volunteer.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'view_volunteerdetail.html',locals())

def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="accept")
    return render(request, 'accepted_volunteer.html',locals())

def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="reject")
    return render(request, 'rejected_volunteer.html',locals())

def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.all()
    return render(request, 'all_volunteer.html',locals())


def view_all_volunteer(request,pid): #the view details show trough id
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.get(id=pid) #get is use for fetching a single data
    return render(request, 'view_all_volunteer.html',locals())

def accepted_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.filter(status="accept")
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)

        try:
            donation.donationarea = da
            donation.volunteer = v
            donation.status = "Volunteer Allocated"
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'accepted_donationdetail.html',locals())

def collection_req(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer,status="Volunteer Allocated")
    return render(request, 'collection_req.html',locals())


def donationcollection_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        volunteerremark = request.POST['volunteerremark']

        try:

            donation.status = status
            donation.volunteerremark = volunteerremark
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'donationcollection_detail.html',locals())

def volunteer_allocated(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    donation = Donation.objects.filter(status="Volunteer Allocated")
    return render(request, 'volunteer_allocated.html', locals())

def allocatedvolunteer_view_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)

        try:
            donation.donationarea = da
            donation.volunteer = v
            donation.status = "Volunteer Allocated"
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'allocatedvolunteer_view_detail.html',locals())

def donationrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer,status="Donation Received")
    return render(request, 'donationrec_volunteer.html',locals())

def donationrec_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']

        try:

            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'donationrec_detail.html',locals())

def donationnotrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer,status="Donation NotReceived")
    return render(request, 'donationnotrec_volunteer.html',locals())

def donationdelivered_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer,status="Donation Delivered")
    return render(request, 'donationdelivered_volunteer.html',locals())












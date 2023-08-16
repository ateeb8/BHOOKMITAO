"""foodwastemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodwaste.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin123/', admin.site.urls),
    path('',index,name='index'),
    path('all_logins',all_logins,name='all_logins'),
    path('donor_login',donor_login,name='donor_login'),
    path('admin_login',admin_login,name='admin_login'),
    path('volunteer_login',volunteer_login,name='volunteer_login'),
    path('donor_reg',donor_reg,name='donor_reg'),
    path('donor_home',donor_home,name='donor_home'),
    path('admin_home',admin_home,name='admin_home'),
    path('volunteer_home',volunteer_home,name='volunteer_home'),
    path('pending_donation',pending_donation,name='pending_donation'),
    path('accepted_donation', accepted_donation, name='accepted_donation'),
    path('add_area', add_area, name='add_area'),
    path('manage_area', manage_area, name='manage_area'),
    path('manage_donor', manage_donor, name='manage_donor'),
    path('logout/',Logout,name='logout'),
    path('donate_now',donate_now,name='donate_now'),
    path('donation_history',donation_history,name='donation_history'),
    path('read_more',read_more,name='read_more'),
    path('view_donationdetail/<int:pid>',view_donationdetail,name='view_donationdetail'),
    path('delete_donationdetail/<int:pid>',delete_donationdetail,name='delete_donationdetail'),
    path('edit_donationdetail/<int:pid>', edit_donationdetail, name='edit_donationdetail'),
    path('admin_view_donationdetail/<int:pid>',admin_view_donationdetail,name='admin_view_donationdetail'),
    path('edit_area/<int:pid>',edit_area,name='edit_area'),
    path('view_area/<int:pid>',view_area,name='view_area'),
    path('delete_area/<int:pid>',delete_area,name='delete_area'),
    path('delete_donor/<int:pid>',delete_donor,name='delete_donor'),
    path('view_donordetail/<int:pid>',view_donordetail,name='view_donordetail'),
    path('volunteer_registration',volunteer_registration,name='volunteer_registration'),
    path('new_volunteer', new_volunteer, name='new_volunteer'),
    path('view_volunteerdetail/<int:pid>',view_volunteerdetail,name='view_volunteerdetail'),
    path('accepted_volunteer', accepted_volunteer, name='accepted_volunteer'),
    path('rejected_volunteer', rejected_volunteer, name='rejected_volunteer'),
    path('all_volunteer', all_volunteer, name='all_volunteer'),
    path('view_all_volunteer/<int:pid>',view_all_volunteer,name='view_all_volunteer'),
    path('delete_volunteer/<int:pid>',delete_volunteer,name='delete_volunteer'),
    path('accpeted_donationdetail/<int:pid>',accepted_donationdetail,name='accepted_donationdetail'),
    path('collection_req', collection_req, name='collection_req'),
    path('donationcollection_detail/<int:pid>',donationcollection_detail,name='donationcollection_detail'),
    path('volunteer_allocated',volunteer_allocated,name='volunteer_allocated'),
    path('allocatedvolunteer_view_detail/<int:pid>',allocatedvolunteer_view_detail,name='allocatedvolunteer_view_detail'),
    path('donationrec_volunteer', donationrec_volunteer, name='donationrec_volunteer'),
    path('donationrec_detail/<int:pid>',donationrec_detail,name='donationrec_detail'),
    path('donationnotrec_volunteer', donationnotrec_volunteer, name='donationnotrec_volunteer'),
    path('donationdelivered_volunteer', donationdelivered_volunteer, name='donationdelivered_volunteer'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

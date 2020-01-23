# flake8: noqa  # ignored since it is being used in the files
from members.views.FamilyDetails import FamilyDetails
from members.views.ConfirmFamily import ConfirmFamily
from members.views.PersonCreate import PersonCreate
from members.views.PersonUpdate import PersonUpdate
from members.views.WaitingListSetSubscription import WaitingListSetSubscription
from members.views.DeclineInvitation import DeclineInvitation
from members.views.ActivitySignup import ActivitySignup
from members.views.UpdatePersonFromForm import UpdatePersonFromForm
from members.views.EntryPage import EntryPage
from members.views.userCreated import userCreated
from members.views.volunteerSignup import volunteerSignup
from members.views.QuickpayCallback import QuickpayCallback
from members.views.waitinglistView import waitinglistView
from members.views.paymentGatewayErrorView import paymentGatewayErrorView
from members.views.departmentView import departmentView
from members.views.Activities import Activities
from members.views.AdminSignup import AdminSignup

from .department_view import DepartmentDetailView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.utils import timezone
from members.forms import AddressForm

from members.models import Address
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def test_form(request):
    submitted = False
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return HttpResponseRedirect("form")
    else:
        form = AddressForm()
        return render(request, "members/form_test.html", {"form": form})

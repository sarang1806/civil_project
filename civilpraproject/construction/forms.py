from django import forms
from .models import *

class customersform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name','emailids','phoneno','address']

class siteform(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['site_name','customer','pincode','state','city','houseno','roadname','address']

class mastermateriallistform(forms.ModelForm):
    class Meta:
        model = mastermateriallist
        fields = ['materialid','materialname']


class categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryid','categoryname']

class unitmeasurementform(forms.ModelForm):
    class Meta:
        model = unitmeasurement
        fields = ['unitmeasurementid','unitmeasurementname']

class brandform(forms.ModelForm):
    class Meta:
        model = brandlist
        fields = ['brandname','materialnames']


class constructionlevelform(forms.ModelForm):
    class Meta:
        model = constructionlevel
        fields = ['constructionlevelname','description']


class worktypesform(forms.ModelForm):
    class Meta:
        model = worktypes
        fields = ['worktypeid','worktypename','workdescription']


class internaltransferform(forms.ModelForm):
    class Meta:
        model = internaltransfer
        fields = ['executiveengineer','executiveengineernum','sourceclientname','sourceaddress',
                  'destinationclientname','destinationaddress','vehiclename','vehiclenum','drivername',
                  'drivernum','date','material','brand','unit','quantity','transferdate']


class employeeregistrationform(forms.ModelForm):
    class Meta:
        model = employeeregistration
        fields = ['employee_name','employeenum','emailid','phonenum','dateofbirth',
                 'permanentaddress','presentaddress','gender','bloodgroup','status','bankacnum',
                 'qualification','aadharcard','pancard','pfnum','pfeligibledate','licencenum']



class constypeForm(forms.ModelForm):
    class Meta:
        model = constructiontype
        fields = "__all__"

class clientregForm(forms.ModelForm):
    class Meta:
        model = Client_registration
        fields = ['client_name', 'representative_name', 'phone_no', 'email', 'site_address', 'inquiry_date']

class clientinquiryForm(forms.ModelForm):
    class Meta:
        model = ClientInquiry
        fields = "__all__"


# *************************************************


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"

class roughForm(forms.ModelForm):
    class Meta:
        model = RoughDrawing
        fields = "__all__"

class finalForm(forms.ModelForm):
    class Meta:
        model = finaldrawing
        fields = "__all__"


class MasterdataForm(forms.ModelForm):
    class Meta:
        model = masterdata
        fields = "__all__"

class transationForm(forms.ModelForm):
    class Meta:
        model = Taskttransaction
        fields = "__all__"





class WorkProgressForm(forms.ModelForm):
    class Meta:
        model = WorkProgress
        fields = ['photo', 'progress', 'worker_count', 'description']
        widgets = {
            'progress': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
        }



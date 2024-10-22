from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import PersonData
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@staff_member_required
def export_data(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;faliename="export_data.csv"'
    writer=csv.writer(response)
    writer.writerow(['Name','Email'])
    for DataObj in PersonData.objects.all():
        writer.writerow([DataObj.name,DataObj.email])
    return response
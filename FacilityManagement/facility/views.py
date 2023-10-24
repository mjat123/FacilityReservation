import datetime
from re import template

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import FacilityForm, FacilityMainRulesForm, FacilityMainRulesSetForm, FacilityPromoRulesForm, FacilitySubRulesForm, FacilityUpdateForm, Revenue_TransactionForm
from .models import Facility, Facility_MainRules, Facility_MainRules_set, Facility_PromoRules, Facility_PromoRules_set, Facility_SubRules, Facility_SubRules_set, Setting_Facility
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from django.db import IntegrityError, connection
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def set_session(request):
    request.session['username'] = 'myuser'
    return HttpResponse('Session variable set.')

def get_session(request):
    username = request.session.get('username')
    if username:
        return HttpResponse(f'Logged in as: {username}')
    else:
        return HttpResponse('Session variable not found.')
    
# def set_session_fmrules(request):
#     request.session['facility'] = 'facility'
#     return HttpResponse('Session variable set.')


# from django import forms
# from .models import Facility
# from .forms import FacilityForm, FacilityUpdateForm
@csrf_protect
def display_facility(request):
    if request.method == 'POST':
        upform = FacilityUpdateForm(request.POST)
        mform = FacilityForm(request.POST)
        f_id = request.POST.get('id')
        nfacility = request.POST.get('facilityname')
        nrateperhour = request.POST.get('rateperhour')
        ncapacity = request.POST.get('capacity')
        lim_rateperhour = 20
        lim_capacity = 300

        if f_id is None:
            try:
                # if mform.is_valid():
                if Facility.objects.filter(facilityname=nfacility).exists():
                    message = f"{nfacility} already exist"
                    messages.error(request, message)
                    return redirect('facility:facility')
                else:
                    mform.save()
                    new_Facility = Setting_Facility(facility=nfacility)
                    new_Facility.save()
                    message = "Facility added successfully"
                    messages.success(request, message)
                    return redirect('facility:facility')
            except Exception as e:
                return JsonResponse({"error": str(e)})
        else:
            try:
                facility = get_object_or_404(Facility, id=f_id)
                facility.facilityname = nfacility
                facility.rateperhour = nrateperhour
                facility.capacity = ncapacity
                facility.save()
                message = "Facility updated successfully"
                messages.success(request, message)
            except Http404:
                return JsonResponse({"error": "Facility not found"})
            except Exception as e:
                return JsonResponse({"error": str(e)})

        return redirect('facility:facility')
    else:
        facility = Facility.objects.all().order_by('id')
        upform = FacilityUpdateForm()
        mform = FacilityForm()

    return render(request, 'facility.html', {'facility': facility, 'upform': upform, 'mform': mform})

@csrf_protect
def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        facility = request.POST['facilityname']
        if form.is_valid():
            form.save()
            new_Facility = Setting_Facility(facility=facility)
            new_Facility.save()
            return redirect('facility:facility')
    else:
        form = FacilityForm()

    return render(request, 'add_facility.html',{'form': form})

@csrf_protect
def delete_facility(request, id):
    f_id = request.POST.get('id')
    try:
        facility = Facility.objects.get(pk=int(id))
        facility.delete()
        sfacility = Setting_Facility.objects.get(facility=facility)
        sfacility.delete()
    except Facility.DoesNotExist:
        # Handle the case where the Facility does not exist
        pass
    except Setting_Facility.DoesNotExist:
        # Handle the case where the associated Setting_Facility does not exist
        pass

    return redirect(reverse('facility:facility'))

@csrf_protect
def display_calendar(request):
     return render(request, 'calendar.html')

@csrf_protect
def display_setting_facility(request):
    setting_facility = Setting_Facility.objects.all().order_by('id')
    # facility = Setting_Facility.objects.all().filter(facility=setting_facility)
    # fmainrules = Facility_MainRules_set.objects.all().filter(facility=facility).order_by('-modified_at')
    return render(request, 'setting.html', {'setting_facility': setting_facility,})

@csrf_protect
def displayall_setting_facility(request):
    setting_facility = Setting_Facility.objects.all().order_by('id')    
    return render(request, 'facility_table.html', {'setting_facility': setting_facility})

@csrf_protect
def set_facility_session(request, facility_id):
    # Set the 'facility_id' session variable to the clicked facility's ID
    request.session['facility_id'] = facility_id
    return redirect('facility:listFacilities') 


@csrf_protect
def update_facility(request, id):
    facility = get_object_or_404(Facility, pk=id)
    request.session['faci_id'] = facility.pk
    
    if request.method == 'POST':
        # upform = FacilityUpdateForm(request.POST, instance=facility)
        # upform = FacilityUpdateForm(request.POST,initial={'facilityname': facility.facilityname, 'rateperhour':facility.rateperhour, 'capacity':facility.capacity})
        upform = FacilityUpdateForm(request.POST, instance=facility)
        new_facility = request.POST.get('facilityname') 
        if upform.is_valid():
            # upform = FacilityUpdateForm(request.POST)
            upform.save()

            with connection.cursor() as cursor:
            # Define the SQL UPDATE statement with placeholders
                sql = """
                UPDATE `facility_setting_facility` 
                SET `facility` = %s 
                WHERE `facility_setting_facility`.`id` = %s
                """

            # Execute the SQL statement with the new values
                cursor.execute(sql, [new_facility, id])
            return redirect('facility:facility')

    else:
        facility = get_object_or_404(Facility, pk=id)
        upform = FacilityUpdateForm(instance=facility)
    
    return render(request, 'update_facility.html',{'upform': upform, 'facility':facility})
    # return HttpResponseRedirect(reverse(request,'facility:updatefacility',{'upform': upform, 'facility': facility}))
    # return render(request, 'facility.html',)
# changed

@csrf_protect
def update_setting_facility(request, id):
    s_facility = get_object_or_404(Setting_Facility, pk=id)
    
    if request.method == 'POST':
        sform = FacilityUpdateForm(request.POST, instance=s_facility)
        if sform.is_valid():
            sform.save()
            return redirect('facility:facility')

    else:
        form = FacilityUpdateForm(instance=s_facility)

    return render(request, 'update_facility.html',{'form': form, 'facility': s_facility})

def is_capacity_within_limit(capacity):
    return int(capacity) <= 20


@csrf_protect
def display_user_mainrules(request, id):
    # facility_id = get_object_or_404(FacilityRules, pk=id)

    template = 'user_mainrules.html'
    return render(request, template)
@csrf_protect
def display_fmrules(request, id):
    facility = get_object_or_404(Setting_Facility, pk=id)
    if request.method == 'POST':
        upform = FacilityUpdateForm(request.POST, instance=facility)
        new_facility = request.POST.get('facilityname') 
        if upform.is_valid():
            upform.save()

            with connection.cursor() as cursor:
            # Define the SQL UPDATE statement with placeholders
                sql = """
                UPDATE `facility_setting_facility` 
                SET `facility` = %s 
                WHERE `facility_setting_facility`.`id` = %s
                """

            # Execute the SQL statement with the new values
                cursor.execute(sql, [new_facility, id])
            return redirect('facility:facility')

    else:
        facility = get_object_or_404(Facility, pk=id)
        upform = FacilityUpdateForm(instance=facility)

    return render(request, 'update_facility.html',{'upform': upform, 'facility': facility})

@csrf_protect
def display_facility_mainrules(request, id):
    sfacility = get_object_or_404(Setting_Facility, pk=id)
    request.session['faci_id'] = sfacility.pk
    request.session['facility'] = sfacility.facility
    template = 'facility_mainrules.html'
    addedmainrules = Facility_MainRules.objects.all().order_by('-created_at')
    fmainrules = Facility_MainRules_set.objects.all().filter(facility=sfacility).order_by('-modified_at')
    
    if request.method == 'POST':
        mform = FacilityMainRulesForm(request.POST)
        if mform.is_valid():
            mform.save()
            
    else:
        # Set the initial value of the 'facility' field in the form
        mform = FacilityMainRulesForm(initial={'facility': sfacility.facility}) 

    return render(request, template, {'sfacility': sfacility, 'fmainrules': fmainrules, 'addedmainrules': addedmainrules,'mform': mform})
# from django.http import HttpResponseRedirect
# from django.urls import reverse

@csrf_protect
def facilitymainrules_set(request, id):
    mainrules = get_object_or_404(Facility_MainRules, pk=id)
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
    newfacility = request.POST.get('facility', facility)
    title = request.POST.get('title',mainrules.title)
    points = request.POST.get('points',mainrules.points)
    num_pc = request.POST.get('num_pc',mainrules.num_pc)
    num_attendies = request.POST.get('num_attendies',mainrules.num_attendies)
    description = request.POST.get('description', mainrules.description)
    rate = request.POST.get('rate', mainrules.rate)
    status = 0
    # new_Facility = Facility_MainRules_set(facility=newfacility, title=title, description=description, rate=rate, status=status)
    if Facility_MainRules_set.objects.filter(facility=newfacility).exists():
        # Facility exists, check if title is different
        if not Facility_MainRules_set.objects.filter(title=title).exists():
            new_Facility = Facility_MainRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description,  rate=rate, status=status)
            new_Facility.save()

    # elif Facility_MainRules_set.objects.filter(facility=newfacility).exists():
    #     if Facility_MainRules_set.objects.filter(status=0).exists():
    #         if not Facility_MainRules_set.objects.filter(title=title).exists():
    #             new_Facility = Facility_MainRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description,  rate=rate, status=status)
    #             new_Facility.save()
    else:
        # Facility doesn't exist, check if title exists
        if Facility_MainRules_set.objects.filter(title=title).exists():
            new_Facility = Facility_MainRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description,  rate=rate, status=status)
            new_Facility.save()

        elif Facility_MainRules_set.objects.filter(status=0).exists():
            new_Facility = Facility_MainRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description,  rate=rate, status=status)
            new_Facility.save()
        else:
            # Neither facility nor title exist
            new_Facility = Facility_MainRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description,  rate=rate, status=status)
            new_Facility.save()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_mainrules.html'))
@csrf_protect
def is_setfacilitymainrules_status(request):
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
    # setting_facility = Setting_Facility.objects.filter(facility=facility)
    mainrules_list = Facility_MainRules_set.objects.filter(facility=facility)
    
    # Update the status for all matching instances
    # setting_facility.save()
    mainrules_list.update(status=1)
    # mainrules.save()
    message = f"The status for {mainrules_list.count()} facilities with the name {facility} has been updated to 1."

    messages.success(request, message)

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_mainrules.html'))
@csrf_protect
def delete_setfacilitymainrules_status(request, id):
    mainrules = get_object_or_404(Facility_MainRules_set, pk=id)
    faci_id = request.session.get('faci_id')
    mainrules.delete()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_mainrules.html'))
        # return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))
@csrf_protect
def delete_facilitymainrules(request, id):
    facility = Facility_MainRules.objects.get(pk=int(id))
    faci_id = request.session.get('faci_id')

    facility.delete()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_mainrules.html'))
        # return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))

# -----------------------------------------SUB RULES-----------------------------------------
@csrf_protect
def display_facility_subrules(request, id):
    sfacility = get_object_or_404(Setting_Facility, pk=id)
    request.session['faci_id'] = sfacility.pk
    request.session['facility'] = sfacility.facility
    template = 'facility_subrules.html'
    addedsubrules = Facility_SubRules.objects.all().order_by('-created_at')
    fsubrules = Facility_SubRules_set.objects.all().filter(facility=sfacility).order_by('-modified_at')
    
    if request.method == 'POST':
        sform = FacilitySubRulesForm(request.POST)
        if sform.is_valid():
            sfacility
            sform.save()
            
    else:
        # Set the initial value of the 'facility' field in the form
        sform = FacilitySubRulesForm(initial={'facility': sfacility.facility}) 

    return render(request, template, {'sfacility': sfacility, 'fsubrules': fsubrules, 'addedsubrules': addedsubrules,'sform': sform})

# is_setfacilitysubrules_status
@csrf_protect
def is_setfacilitysubrules_status(request):
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
    mainrules_list = Facility_SubRules_set.objects.filter(facility=facility)
    # Update the status for all matching instances
    mainrules_list.update(status=1)
    # mainrules.save()
    message = f"The status for {mainrules_list.count()} facilities with the name {facility} has been updated to 1."

    messages.success(request, message)

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilitysubrules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_subrules.html'))

@csrf_protect
def facilitysubrules_set(request, id):
    subrules = get_object_or_404(Facility_SubRules, pk=id)
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
        
    newfacility = request.POST.get('facility', facility)
    title = request.POST.get('title',subrules.title)
    description = request.POST.get('description', subrules.description)
    status = 0
    # new_Facility = Facility_SubRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description, rate=rate, status=status)
    if Facility_SubRules_set.objects.filter(facility=newfacility).exists():
        # Facility exists, check if title is different
        if not Facility_SubRules_set.objects.filter(title=title).exists():
            new_Facility = Facility_SubRules_set(facility=newfacility, title=title, description=description, status=status)
            new_Facility.save()
   
    
    else:
        # Facility doesn't exist, check if title exists
        if Facility_SubRules_set.objects.filter(title=title).exists():
            new_Facility = Facility_SubRules_set(facility=newfacility, title=title, description=description, status=status)
            new_Facility.save()

        elif Facility_SubRules_set.objects.filter(status=0).exists():
            new_Facility = Facility_SubRules_set(facility=newfacility, title=title, description=description, status=status)
            new_Facility.save() 

        else:
            # Neither facility nor title exist
            new_Facility = Facility_SubRules_set(facility=newfacility, title=title, description=description, status=status)
            new_Facility.save()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilitysubrules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_subrules.html'))
    

@csrf_protect
def delete_setfacilitysubrules_status(request, id):
    subrules = get_object_or_404(Facility_SubRules_set, pk=id)
    faci_id = request.session.get('faci_id')
    subrules.delete()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilitysubrules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_subrules.html'))
        # return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))

# -------------------------------promo rules----------------------------------------------------
@csrf_protect
def display_facility_promorules(request, id):
    sfacility = get_object_or_404(Setting_Facility, pk=id)
    request.session['faci_id'] = sfacility.pk
    request.session['facility'] = sfacility.facility
    template = 'facility_promorules.html'
    addedpromorules = Facility_PromoRules.objects.all().order_by('-created_at')
    fpromorules = Facility_PromoRules_set.objects.all().filter(facility=sfacility).order_by('-modified_at')
    
    if request.method == 'POST':
        pform = FacilityPromoRulesForm(request.POST)
        if pform.is_valid():
            sfacility
            pform.save()
            
    else:
        # Set the initial value of the 'facility' field in the form
        pform = FacilityPromoRulesForm(initial={'facility': sfacility.facility}) 

    return render(request, template, {'sfacility': sfacility, 'fpromorules': fpromorules, 'addedpromorules': addedpromorules,'pform': pform})

# is_setfacilitysubrules_status
@csrf_protect
def is_setfacilitypromorules_status(request):
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
    promorules_list = Facility_PromoRules_set.objects.filter(facility=facility)
    # Update the status for all matching instances
    promorules_list.update(status=1)
    # promorules.save()
    message = f"The status for {promorules_list.count()} facilities with the name {facility} has been updated to 1."

    messages.success(request, message)

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilitypromorules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_promorules.html'))

@csrf_protect
def facilitypromorules_set(request, id):
    promorules = get_object_or_404(Facility_PromoRules, pk=id)
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
        
    newfacility = request.POST.get('facility', facility)
    title = request.POST.get('title',promorules.title)
    description = request.POST.get('description', promorules.description)
    new_rate = request.POST.get('new_rate',promorules.new_rate)
    start_date = request.POST.get('start_date',promorules.start_date)
    end_date = request.POST.get('end_date',promorules.end_date)
    capacity = request.POST.get('capacity',promorules.capacity)
    status = 0
    # new_Facility = Facility_SubRules_set(facility=newfacility, title=title, points=points, num_pc=num_pc, num_attendies=num_attendies, description=description, rate=rate, status=status)
    if Facility_PromoRules_set.objects.filter(facility=newfacility).exists():
        # Facility exists, check if title is different
        if not Facility_PromoRules_set.objects.filter(title=title).exists():
            new_Facility = Facility_PromoRules_set(facility=newfacility, title=title, description=description, new_rate=new_rate, start_date=start_date, end_date=end_date, capacity=capacity, status=status)
            new_Facility.save()
   
    
    else:
        # Facility doesn't exist, check if title exists
        if Facility_PromoRules_set.objects.filter(title=title).exists():
            new_Facility = Facility_PromoRules_set(facility=newfacility, title=title, description=description, new_rate=new_rate, start_date=start_date, end_date=end_date, capacity=capacity, status=status)
            new_Facility.save()

        elif Facility_PromoRules_set.objects.filter(status=0).exists():
            new_Facility = Facility_PromoRules_set(facility=newfacility, title=title, description=description, new_rate=new_rate, start_date=start_date, end_date=end_date, capacity=capacity, status=status)
            new_Facility.save() 
            
        else:
            # Neither facility nor title exist
            new_Facility = Facility_PromoRules_set(facility=newfacility, title=title, description=description, new_rate=new_rate, start_date=start_date, end_date=end_date, capacity=capacity, status=status)
            new_Facility.save()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilitypromorules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_promorules.html'))
    

@csrf_protect
def delete_setfacilitypromorules_status(request, id):
    promorules = get_object_or_404(Facility_PromoRules_set, pk=id)
    faci_id = request.session.get('faci_id')
    promorules.delete()

    if faci_id is not None:
        return HttpResponseRedirect(reverse('facility:facilitypromorules', args=[faci_id]))
    else:
        # Handle the case when faci_id is None, e.g., by redirecting to a default URL
        return HttpResponseRedirect(reverse('facility_promorules.html'))
        # return HttpResponseRedirect(reverse('facility:facilityRules', args=[faci_id]))
@csrf_protect
def display_facility_promo(request, id):
    sfacility = get_object_or_404(Setting_Facility, pk=id)
    faci_id = request.session.get('faci_id')
    facility = request.session.get('facility')
    template = 'facility_promorules.html'
    addedpromorules = Facility_PromoRules.objects.all().order_by('-created_at')
    fpromorules = Facility_PromoRules.objects.all().filter(facility=sfacility).order_by('-modified_at')
    
    if request.method == 'POST':
        pform = FacilityPromoRulesForm(request.POST)
        if pform.is_valid():
            pform.save()
            
    else:
        # Set the initial value of the 'facility' field in the form
        pform = FacilitySubRulesForm(initial={'facility': sfacility.facility}) 

    return render(request, template, {'sfacility': sfacility, 'fpromorules': fpromorules, 'addedpromorules': addedpromorules,'pform': pform})

@csrf_protect
def revenue_report(request):
    revenue_trans = Revenue_TransactionForm()    
    return render(request, 'revenue_report.html', {'revenue_trans': revenue_trans})

@csrf_protect
def revenue_dashboard(request):
    revenue_trans = Revenue_TransactionForm()    
    return render(request, 'revenue_dashboard.html', {'revenue_trans': revenue_trans})

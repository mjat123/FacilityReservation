# from FacilityManagement.facility import facility
from . import views
from django.urls import path
# from .views import put
app_name ='facility'

urlpatterns =[
    path('facility', views.display_facility, name='facility'),
    path('updatefaci', views.display_facility, name='updatefaci'),
    path('addfacility', views.add_facility, name='addfacility'),
    path('deleteFacility/<int:id>', views.delete_facility, name='deleteFacility'),
    path('updateFacility/<int:id>', views.update_facility, name='updatefacility'),
    path('facilitytable', views.displayall_setting_facility, name='facilitytable'), 

    # path('sessfaci/<int:id>', views.set_session_facility, name='sessfaci'),

    path('facilityRules/<int:id>', views.display_facility_mainrules, name='facilityRules'),
    path('delfmrules/<int:id>', views.delete_facilitymainrules, name='delfmrules'),    
    path('setfmstatus/<int:id>', views.facilitymainrules_set, name='setfmstatus'),
    path('delfmstatus/<int:id>', views.delete_setfacilitymainrules_status, name='delfmstatus'),
# status to 1
    path('setfmstatus_one/', views.is_setfacilitymainrules_status, name='setfmstatus_one'),
    path('userMainRules/<int:id>', views.display_user_mainrules, name='userMainRules'),

    path('settingfacility', views.display_setting_facility, name='settingfacility'),
    path('updatesettingfacility/<int:id>', views.update_setting_facility, name='settingfacility'),

    path('facilitySubrules/<int:id>', views.display_facility_subrules, name='facilitysubrules'),
    path('setfsstatus_one/', views.is_setfacilitysubrules_status, name='setfsstatus_one'),
    path('setfsstatus/<int:id>', views.facilitysubrules_set, name='setfsstatus'),
    path('delfsstatus/<int:id>', views.delete_setfacilitysubrules_status, name='delfsstatus'),

    path('facilityPromrules/<int:id>', views.display_facility_promorules, name='facilitypromorules'),
    path('setfpstatus_one/', views.is_setfacilitypromorules_status, name='setfpstatus_one'),
    path('setfpstatus/<int:id>', views.facilitypromorules_set, name='setfpstatus'),
    path('delfpstatus/<int:id>', views.delete_setfacilitypromorules_status, name='delfpstatus'),


    path('calendar', views.display_calendar, name='calendar'),

    
    path('dashboard', views.revenue_dashboard, name='revenuedashboard'),
    path('report', views.revenue_report, name='revenuereport'),



    
]
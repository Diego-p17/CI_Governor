from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [


    # -- Genreral -- #
    path('general/', views.get_general, name= "general"),
    # Country
    path('general/addCountry', views.addCountry, name= "addCountry"),
    path('general/deleteCountry/<int:id_Country>', views.deleteCountry, name= "deleteCountry"),
    path('general/updateCountry/<int:id_Country>', views.updateCountry, name= "updateCountry"),
    # City
    path('general/addCity', views.addCity, name= "addCity"),
    path('general/deleteCity/<int:id_City>', views.deleteCity, name= "deleteCity"),
    path('general/updateCity/<int:id_City>', views.updateCity, name= "updateCity"),
    #Os
    path('general/addOs', views.addOs, name= "addOs"),
    path('general/deleteOs/<int:id_Os>', views.deleteOs, name= "deleteOs"),
    path('general/updateOS/<int:id_Os>', views.updateOs, name= "updateOs"),
    #Platform
    path('general/addPlatform', views.addPlatform, name= "addPlatform"),
    path('general/deletePlatform/<int:id_Platform>', views.deletePlatform, name= "deletePlatform"),
    path('general/updatePlatform/<int:id_Platform>', views.updatePlatform, name= "updatePlatform"),
    #DeviceType
    path('general/addDeviceType', views.addDeviceType, name= "addDeviceType"),
    path('general/deleteDeviceType/<int:id_DeviceType>', views.deleteDeviceType, name= "deleteDeviceType"),
    path('general/updateDeviceType/<int:id_DeviceType>', views.updateDeviceType, name= "updateDeviceType"),
    #TokenType
    path('general/addTokenType', views.addTokenType, name= "addTokenType"),
    path('general/deleteTokenType/<int:id_TokenType>', views.deleteTokenType, name= "deleteTokenType"),
    path('general/updateTokenType/<int:id_TokenType>', views.updateTokenType, name= "updateTokenType"),
    #Settings type
    path('general/addSettingsType', views.addSettingsType, name= "addSettingsType"),
    path('general/deleteSettingsType/<int:id_SettingsType>', views.deleteSettingsType, name= "deleteSettingsType"),
    path('general/updateSettingsType/<int:id_SettingsType>', views.updateSettingsType, name= "updateSettingsType"),

    #################
    # Organizations #
    #################
    path('', views.get_allOrganizations, name= "home"),
    path('organization/<int:idOrg>/', views.get_organization, name = "organization"),
    path('form_organization/', views.form_addOrganization, name = "form_addOrganization"),
    path('add_organization/', views.add_organization, name = "add_organization"),
    path('update_organization/<int:idOrg>', views.update_organization, name = "update_organization"),

    #PeopleORG
    path('add_peopleOrg/<int:idOrg>/', views.add_peopleOrg, name = "add_peopleOrg"),
    path('delete_peopleOrg/<int:idPeople>/<int:idOrganization>/', views.delete_peopleOrg, name="delete_peopleOrg"),
    #SitesOrg
    path('add_siteOrg/<int:idOrg>/', views.add_siteOrg, name = "add_siteOrg"),
    path('delete_orgSite/<int:idSite>', views.delete_orgSite, name = "delete_orgSite"),

    ###########
    #  Sites  #
    ###########
    path('sites/', views.sites, name = "sites"),
    path('site/<int:idSite>/', views.site_info, name = "site_info"),
    path('form_site/', views.form_site, name = "form_site"),
    path('add_site/', views.add_site, name = "add_site"),
    path('update_site/<int:idSite>', views.update_site, name = "update_site"),
    #zoneSite
    path('add_zone/<int:idSite>/', views.add_zone, name = "add_zone"),
    path('update_zone/<int:idZone>/', views.update_zone, name = "update_zone"),
    path('delete_zone/<int:idZone>/', views.delete_zone, name = "delete_zone"),

    #############
    #  Peoples  #
    #############
    path('peoples/', views.peoples, name = "peoples"),
    path('people_info/<int:idPeople>', views.people_info, name = "people_info"),
    path('form_people/', views.form_people, name = "form_people"),
    path('add_people/', views.add_people, name = "add_people"),
    path('update_people/<int:idPeople>/', views.update_people, name = "update_people"),
    path('delete_people/<int:idPeople>/', views.delete_people, name = "delete_people"),

    path('permisos_persona/<str:id_persona>/', views.permisos_persona, name = "permisos_persona"),
    path('eliminar_permiso/<str:id_persona>/<int:id_permiso>/', views.eliminar_permiso, name="eliminar_permiso"),
    path('modificar_permiso/<str:id_persona>/<int:id_permiso>/', views.modificar_permiso, name="modificar_permiso"),
    path('formulario_permisos/<str:id_persona>/', views.formulario_permisos, name = "formulario_permisos"),
    path('guardar_permiso/<str:id_persona>', views.guardar_permiso, name="guardar_permiso"),
    path('guardar_modificar_permiso/<str:id_persona>/<int:id_permiso>', views.guardar_modificar_permiso, name = "guardar_modificar_permiso"),


    ##################
    #  Dispositivos  #
    ##################
    path('devices/', views.devices, name = "devices"),
    path('add_device/', views.add_device, name = "add_device"),
    path('formulario_actualizar_dispositivo/<int:id_device>/', views.formulario_actualizar_dispositivo, name="formulario_actualizar_dispositivo"),
    path('actualizar_dispositivo/<int:id_device>/', views.actualizar_dispositivo, name ="actualizar_dispositivo"),
    path('delete_device/<int:idDevice>/', views.delete_device, name = "delete_device"),

]

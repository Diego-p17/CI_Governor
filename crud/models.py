# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#-----------------#
# General Tables  #
#-----------------#

#-- TABLE CITY --#
class TbCity(models.Model):
    id_City    = models.AutoField(db_column='id_City', primary_key=True)
    nameCity   = models.CharField(db_column='nameCity' , max_length=255)
    id_Country = models.ForeignKey('TbCountry', db_column='id_Country' , on_delete=models.PROTECT)

    def __str__(self):
        return self.nameCity
    class Meta:
        managed  = True
        db_table = 'Tb_City'


#-- TABLE COUNTRY --#
class TbCountry(models.Model):
    id_Country  = models.AutoField(db_column='id_Country', primary_key=True)
    nameCountry = models.CharField(db_column='nameCountry',  max_length=255)

    def __str__(self):
        return self.nameCountry
    class Meta:
        managed  = True
        db_table = 'Tb_Country'

#-- TABLE DEVICETYPE --#
class TbDeviceType(models.Model):
    id_DeviceType  = models.AutoField(db_column='id_DeviceType', primary_key=True)
    nameDeviceType = models.CharField(db_column='nameDeviceType', max_length=255)

    def __str__(self):
        return self.nameDeviceType
    class Meta:
        managed  = True
        db_table = 'Tb_DeviceType'

#-- TABLE HwPlatform --#
class TbHwPlatform(models.Model):
    id_HwPlatform  = models.AutoField(db_column='id_HwPlatform', primary_key=True)
    nameHwPlatform = models.CharField(db_column='nameHwPlatform', max_length=255)

    def __str__(self):
        return self.nameHwPlatform
    class Meta:
        managed  = True
        db_table = 'Tb_HwPlatform'


#-- TABLE OS --#
class TbOs(models.Model):
    id_Os  = models.AutoField(db_column='Id_Os', primary_key=True)
    nameOs = models.CharField(db_column='nameOs', max_length=255)

    def __str__(self):
        return self.nameOs
    class Meta:
        managed  = True
        db_table = 'Tb_Os'

#-- TABLE TokenType --#
class TbTokenType(models.Model):
    id_TokenType  = models.AutoField(db_column='id_TokenType', primary_key=True)
    nameTokenType = models.CharField(db_column='nameTokenType', max_length=255 )

    def __str__(self):
        return self.nameTokenType
    class Meta:
        managed  = True
        db_table = 'Tb_TokenType'

#-- TABLE TbSettingsType --#
class TbSettingsType(models.Model):
    id_SettingsType  = models.AutoField(db_column='id_SettingsType', primary_key=True)
    nameSettingsType = models.CharField(db_column='nameSettingsType', max_length=255)

    def __str__(self):
        return self.nameSettingsType
    class Meta:
        managed  = True
        db_table = 'Tb_SettingsType'

#-----------------#
# Entitys Tables  #
#-----------------#

#-- TABLE TbOrganization --#
class TbOrganization(models.Model):
    id_Organization          = models.AutoField(db_column='id_Organization', primary_key=True)
    nameOrganization         = models.CharField(db_column='nameOrganization', max_length=255)
    taxIdOrganization        = models.CharField(db_column='taxIdOrganization', max_length=255)
    addressOrganization      = models.CharField(db_column='addressOrganization', max_length=255)
    contactEmailOrganization = models.CharField(db_column='contactEmailOrganization', max_length=255)
    isActive                 = models.BooleanField(db_column= 'isActive', default=True)

    # Dependencies tables
    id_Country               = models.ForeignKey('TbCountry', db_column='id_Country' , on_delete=models.PROTECT)
    id_City                  = models.ForeignKey('TbCity', db_column='id_City', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameOrganization
    class Meta:
        managed  = True
        db_table = 'Tb_Organization'
#-- TABLE TbSite --#
class TbSite(models.Model):
    id_Site      = models.AutoField(db_column='id_Site', primary_key=True)
    nameSite     = models.CharField(db_column='nameSite', max_length=255)
    addressSite  = models.CharField(db_column='addressSite', max_length=255)
    isActive     = models.BooleanField(db_column= 'isActive', default=True)

    # Dependencies tables
    id_Organization = models.ForeignKey('TbOrganization', db_column='id_Organization', on_delete=models.PROTECT)
    id_Country      = models.ForeignKey('TbCountry', db_column='id_Country' , on_delete=models.PROTECT)
    id_City         = models.ForeignKey('TbCity', db_column='id_City', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameSite
    class Meta:
        managed  = True
        db_table = 'Tb_Site'

#-- TABLE TbZone --#
class TbZone(models.Model):
    id_Zone  = models.AutoField(db_column='id_Zone', primary_key=True)
    nameZone = models.CharField(db_column='nameZone', max_length=255)

    # Dependencies tables
    id_Site = models.ForeignKey('TbSite', db_column='id_Site', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameZone
    class Meta:
        managed  = True
        db_table = 'Tb_Zone'

#-- TABLE TbPeople --#
class TbPeople(models.Model):
    id_People    = models.AutoField(db_column='id_People', primary_key=True)
    namePeople   = models.CharField(db_column='namePeople', max_length=255)
    emailPeople  = models.CharField(db_column='emailPeople', max_length=255)
    phonePeople  = models.IntegerField(db_column='phonePeople')

    # Dependencies tables
    id_Organization = models.ForeignKey('TbOrganization', db_column='id_Organization', on_delete=models.PROTECT)

    def __str__(self):
        return self.namePeople
    class Meta:
        managed  = True
        db_table = 'Tb_People'

#-- TABLE TbDevice --#
class TbDevice(models.Model):
    id_Device           = models.AutoField(db_column='id_Device', primary_key=True)
    nameDevice          = models.CharField(db_column='nameDevice', max_length=255)
    tokenDevice         = models.CharField(db_column='tokenDevice', max_length=255)
    creationDateDevice  = models.DateTimeField(db_column='creationDateDevice')

    # Dependencies tables
    id_hwPlatform   = models.ForeignKey('TbHwPlatform', db_column='id_HwPlatform', on_delete=models.PROTECT)
    id_Os           = models.ForeignKey('TbOs', db_column='id_Os', on_delete=models.PROTECT)
    id_DeviceType   = models.ForeignKey('TbDeviceType', db_column='id_DeviceType', on_delete=models.PROTECT)
    id_Organization = models.ForeignKey('TbOrganization', db_column='id_Organization', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameDevice
    class Meta:
        managed  = True
        db_table = 'Tb_Device'

#-- TABLE TbToken --#
class TbToken(models.Model):
    id_Token   = models.AutoField(db_column='id_Token', primary_key=True)
    valueToken = models.CharField(db_column='valueToken', max_length=255)
    id_Owner   = models.IntegerField(db_column='id_Owner')
    # Dependencies tables
    id_TokenType = models.ForeignKey('TbTokenType', db_column='id_TokenType' , on_delete=models.PROTECT)

    def __str__(self):
        return self.valueToken
    class Meta:
        managed  = True
        db_table = 'Tb_Token'

#-- TABLE TbLocalization --#
class TbLocalization(models.Model):
    id_Localization = models.AutoField(db_column='id_Localization', primary_key=True)
    gpsDataLocation = models.CharField(db_column='gpsDataLocation', max_length=255)
    isActive        = models.BooleanField(db_column='isActive', default=True)
    # Dependencies tables
    id_Device = models.ForeignKey('TbDevice', db_column='id_Device', on_delete=models.PROTECT)
    idZone    = models.ForeignKey('TbZone', db_column='id_Zone', on_delete=models.PROTECT)

    def __str__(self):
        return self.gpsDataLocation
    class Meta:
        managed  = True
        db_table = 'Tb_Localization'

#-- TABLE TbAplication --#
class TbAplication(models.Model):
    id_Aplication = models.AutoField(db_column='id_Aplication', primary_key=True)
    nameAplication = models.CharField(db_column='nameAplication', max_length=255)
    sectionAplication = models.CharField(db_column='sectionAplication', max_length= 255)

    def __str__(self):
        return self.nameAplication
    class Meta:
        managed  = True
        db_table = 'Tb_Aplication'


#-- TABLE TbAutorization --#
class TbAutorization(models.Model):
    id_Autorization   = models.AutoField(db_column='id_Autorization', primary_key=True)
    sectionAutorization = models.CharField(db_column='sectionAutorization', max_length= 255)
    # Dependencies tables
    id_People     = models.ForeignKey('TbPeople', db_column='id_People', on_delete=models.PROTECT)
    id_Device     = models.ForeignKey('TbDevice', db_column='id_Device', on_delete=models.PROTECT)
    id_Aplication = models.ForeignKey('TbAplication', db_column='id_Aplication', on_delete=models.PROTECT)

    def __str__(self):
        return self.sectionAutorization
    class Meta:
        managed  = True
        db_table = 'Tb_Autorization'

#-- TABLE TbSettings --#
class TbSettings(models.Model):
    id_Settings   = models.AutoField(db_column='id_Setting', primary_key=True)
    id_Owner      = models.IntegerField(db_column='id_Owner')
    valueSettings = models.CharField(db_column='valueSettings', max_length=255)
    # Dependencies tables
    id_SettingsType = models.ForeignKey('TbSettingsType', db_column='id_SettingsType', on_delete=models.PROTECT)

    def __str__(self):
        return self.valueSettings
    class Meta:
        managed  = True
        db_table = 'Tb_Settings'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#General Tables

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
        db_table = 'TB_HwPlatform'


#-- TABLE OS --#
class TbOs(models.Model):
    id_Os  = models.AutoField(db_column='Id_Os', primary_key=True)
    nameOs = models.CharField(db_column='nameOs', max_length=255)

    def __str__(self):
        return self.nameOs
    class Meta:
        managed  = True
        db_table = 'TB_Os'

#-- TABLE TokenType --#
class TbTokenType(models.Model):
    id_TokenType  = models.AutoField(db_column='id_TokenType', primary_key=True)
    nameTokenType = models.CharField(db_column='nameTokenType', max_length=255 )

    def __str__(self):
        return self.nameTokenType
    class Meta:
        managed  = True
        db_table = 'TB_TokenType'

#-- TABLE TbSettingsType --#
class TbSettingsType(models.Model):
    id_SettingsType  = models.AutoField(db_column='id_SettingsType', primary_key=True)  # Field name made lowercase.
    nameSettingsType = models.CharField(db_column='nameSettingsType', max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.nameSettingsType
    class Meta:
        managed  = True
        db_table = 'TB_settingsType'

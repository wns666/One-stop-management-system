# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class WAdmin(models.Model):
    w_adno = models.CharField(primary_key=True, max_length=50)
    w_pass = models.CharField(max_length=20)
    w_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_admin'


class WDist(models.Model):
    w_no = models.CharField(primary_key=True, max_length=50)
    w_name = models.CharField(max_length=50)
    w_mno = models.CharField(max_length=20)
    w_class = models.CharField(max_length=20, blank=True, null=True)
    w_ano = models.CharField(max_length=50, blank=True, null=True)
    w_dno = models.CharField(max_length=10, blank=True, null=True)
    w_dorm = models.CharField(max_length=10, blank=True, null=True)
    w_sex = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_dist'


class WInform(models.Model):
    w_ano = models.CharField(primary_key=True, max_length=50)
    w_l1 = models.CharField(max_length=50, blank=True, null=True)
    w_l2 = models.CharField(max_length=50, blank=True, null=True)
    w_l3 = models.CharField(max_length=50, blank=True, null=True)
    w_l4 = models.CharField(max_length=50, blank=True, null=True)
    w_l5 = models.CharField(max_length=50, blank=True, null=True)
    w_l6 = models.CharField(max_length=50, blank=True, null=True)
    w_l7 = models.CharField(max_length=50, blank=True, null=True)
    w_l8 = models.CharField(max_length=50, blank=True, null=True)
    w_l9 = models.CharField(max_length=50, blank=True, null=True)
    w_l10 = models.CharField(max_length=50, blank=True, null=True)
    w_l11 = models.CharField(max_length=50, blank=True, null=True)
    w_l12 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_inform'


class WInit(models.Model):
    w_no = models.CharField(primary_key=True, max_length=50)
    w_lno = models.CharField(max_length=50)
    w_name = models.CharField(max_length=50)
    w_sex = models.CharField(max_length=10, blank=True, null=True)
    w_mno = models.CharField(max_length=20)
    w_school = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_init'


class WMajor(models.Model):
    w_mno = models.CharField(primary_key=True, max_length=20)
    w_mname = models.CharField(max_length=30)
    w_dorm = models.CharField(max_length=10, blank=True, null=True)
    w_fee = models.IntegerField(blank=True, null=True)
    w_dorm2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_major'


class WPunish(models.Model):
    w_num = models.AutoField(primary_key=True)
    w_ano = models.CharField(max_length=50)
    w_name = models.CharField(max_length=50)
    w_date = models.CharField(max_length=20, blank=True, null=True)
    w_pl = models.CharField(max_length=20, blank=True, null=True)
    w_thing = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_punish'


class WRecord(models.Model):
    w_num = models.AutoField(primary_key=True)
    w_ano = models.CharField(max_length=50)
    w_name = models.CharField(max_length=50)
    w_date = models.CharField(max_length=20, blank=True, null=True)
    w_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_record'


class WReward(models.Model):
    w_num = models.AutoField(primary_key=True)
    w_ano = models.CharField(max_length=50)
    w_name = models.CharField(max_length=50)
    w_date = models.CharField(max_length=20, blank=True, null=True)
    w_rl = models.CharField(max_length=20, blank=True, null=True)
    w_thing = models.CharField(max_length=100, blank=True, null=True)
    w_rename = models.CharField(max_length=20, blank=True, null=True)
    w_organ = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_reward'


class WRewardApply(models.Model):
    w_num = models.AutoField(primary_key=True)
    w_ano = models.CharField(max_length=50)
    w_name = models.CharField(max_length=50)
    w_date = models.CharField(max_length=20, blank=True, null=True)
    w_rl = models.CharField(max_length=20, blank=True, null=True)
    w_thing = models.CharField(max_length=100, blank=True, null=True)
    w_rename = models.CharField(max_length=20, blank=True, null=True)
    w_organ = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_reward_apply'


class WStup(models.Model):
    w_ano = models.CharField(primary_key=True, max_length=50)
    w_pass = models.CharField(max_length=20)
    w_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_stup'


class WTotal(models.Model):
    w_ano = models.CharField(primary_key=True, max_length=50)
    w_name = models.CharField(max_length=50)
    w_amount1 = models.IntegerField(blank=True, null=True)
    w_amount2 = models.IntegerField(blank=True, null=True)
    w_state = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'w_total'

# Generated by Django 5.1.3 on 2024-11-14 05:46

from django.db import migrations

def forwards_func(apps, schema_editor):
    ServerUptime = apps.get_model("uptime", "ServerUptime")
    db_alias = schema_editor.connection.alias
    ServerUptime.objects.using(db_alias).bulk_create(
        [
            ServerUptime(HostName='Ser01', HostIntIP='115.110.132.01', BootTime='2024-10-17 00:15:44', UpTime='25:06:45:12'),
            ServerUptime(HostName='Ser02', HostIntIP='115.110.132.02', BootTime='2024-10-23 00:49:03', UpTime='19:06:11:58'),
            ServerUptime(HostName='Ser03', HostIntIP='115.110.132.03', BootTime='2024-10-17 23:30:46', UpTime='24:07:30:17'),
            ServerUptime(HostName='Ser04', HostIntIP='115.110.132.04', BootTime='2024-10-24 22:57:36', UpTime='17:08:03:31'),
            ServerUptime(HostName='Ser05', HostIntIP='115.110.132.05', BootTime='2024-10-16 23:50:39', UpTime='25:07:10:32'),
            ServerUptime(HostName='Ser06', HostIntIP='115.110.132.06', BootTime='2024-10-23 00:30:51', UpTime='19:06:30:22'),
        ]        
    )
def reverse_func(apps, schema_editor):
    ServerUptime = apps.get_model("uptime", "ServerUptime")
    db_alias = schema_editor.connection.alias
    ServerUptime.objects.using(db_alias).filter(HostName='Ser01', HostIntIP='115.110.132.01', BootTime='2024-10-17 00:15:44', UpTime='25:06:45:12').delete()
    ServerUptime.objects.using(db_alias).filter(HostName='Ser02', HostIntIP='115.110.132.02', BootTime='2024-10-23 00:49:03', UpTime='19:06:11:58').delete()
    ServerUptime.objects.using(db_alias).filter(HostName='Ser03', HostIntIP='115.110.132.03', BootTime='2024-10-17 23:30:46', UpTime='24:07:30:17').delete()
    ServerUptime.objects.using(db_alias).filter(HostName='Ser04', HostIntIP='115.110.132.04', BootTime='2024-10-24 22:57:36', UpTime='17:08:03:31').delete()
    ServerUptime.objects.using(db_alias).filter(HostName='Ser05', HostIntIP='115.110.132.05', BootTime='2024-10-16 23:50:39', UpTime='25:07:10:32').delete()
    ServerUptime.objects.using(db_alias).filter(HostName='Ser06', HostIntIP='115.110.132.06', BootTime='2024-10-23 00:30:51', UpTime='19:06:30:22').delete()

class Migration(migrations.Migration):

    initial = True

    dependencies = [        
        ("uptime", "0001_initial")
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
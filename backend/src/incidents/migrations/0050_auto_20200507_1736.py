# Generated by Django 2.2.12 on 2020-05-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0049_auto_20200503_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentstatus',
            name='current_status',
            field=models.CharField(choices=[('NEW', 'New'), ('CLOSED', 'Closed'), ('ACTION_TAKEN', 'Action Taken'), ('ACTION_PENDING', 'Action Pending'), ('INFORMATION_PROVIDED', 'Information Provided'), ('INFORMATION_REQUESTED', 'Information Requested'), ('VERIFIED', 'Verified'), ('INVALIDATED', 'Invalidated'), ('REOPENED', 'Reopened')], max_length=50),
        ),
        migrations.AlterField(
            model_name='incidentstatus',
            name='previous_status',
            field=models.CharField(blank=True, choices=[('NEW', 'New'), ('CLOSED', 'Closed'), ('ACTION_TAKEN', 'Action Taken'), ('ACTION_PENDING', 'Action Pending'), ('INFORMATION_PROVIDED', 'Information Provided'), ('INFORMATION_REQUESTED', 'Information Requested'), ('VERIFIED', 'Verified'), ('INVALIDATED', 'Invalidated'), ('REOPENED', 'Reopened')], max_length=50, null=True),
        ),
    ]
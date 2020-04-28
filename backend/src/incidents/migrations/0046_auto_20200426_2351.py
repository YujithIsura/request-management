# Generated by Django 2.2.12 on 2020-04-26 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidents', '0045_auto_20200426_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvideInformationWorkflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('actioned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_provideinformationworkflow_related', related_query_name='incidents_provideinformationworkflows', to=settings.AUTH_USER_MODEL)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_provideinformationworkflow_related', related_query_name='incidents_provideinformationworkflows', to='incidents.Incident')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='requestinformationworkflow',
            old_name='is_advice_provided',
            new_name='is_information_provided',
        ),
        migrations.AlterField(
            model_name='incidentstatus',
            name='current_status',
            field=models.CharField(choices=[('NEW', 'New'), ('CLOSED', 'Closed'), ('ACTION_TAKEN', 'Action Taken'), ('ACTION_PENDING', 'Action Pending'), ('INFORMATION_PROVIDED', 'Information Provided'), ('INFORMATION_REQESTED', 'Information Requested'), ('VERIFIED', 'Verified'), ('INVALIDATED', 'Invalidated'), ('REOPENED', 'Reopened')], max_length=50),
        ),
        migrations.AlterField(
            model_name='incidentstatus',
            name='previous_status',
            field=models.CharField(blank=True, choices=[('NEW', 'New'), ('CLOSED', 'Closed'), ('ACTION_TAKEN', 'Action Taken'), ('ACTION_PENDING', 'Action Pending'), ('INFORMATION_PROVIDED', 'Information Provided'), ('INFORMATION_REQESTED', 'Information Requested'), ('VERIFIED', 'Verified'), ('INVALIDATED', 'Invalidated'), ('REOPENED', 'Reopened')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='ProvideAdviceWorkflow',
        ),
        migrations.AddField(
            model_name='provideinformationworkflow',
            name='initiated_workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='incidents.RequestInformationWorkflow'),
        ),
    ]
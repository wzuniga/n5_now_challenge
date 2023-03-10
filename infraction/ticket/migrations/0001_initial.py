# Generated by Django 4.1.7 on 2023-02-19 03:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identification_number', models.CharField(max_length=8)),
                ('credential_application', models.ForeignKey(db_column='credential_application_id', on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_document', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_plate', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Solo caracteres alphanumericos son permitidos.')])),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('person', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='ticket.person')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments', models.TextField(default='')),
                ('officer', models.ForeignKey(db_column='officer_id', on_delete=django.db.models.deletion.CASCADE, to='ticket.officer')),
                ('person', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='ticket.person')),
                ('vehicle', models.ForeignKey(db_column='vehicle_id', on_delete=django.db.models.deletion.CASCADE, to='ticket.vehicle')),
            ],
        ),
    ]

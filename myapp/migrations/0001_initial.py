# Generated by Django 3.1.4 on 2021-03-04 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=255, unique=True)),
                ('county', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('system_type', models.CharField(choices=[('C', 'Community'), ('NC', 'Non-Community'), ('NP', 'Irrigation'), ('TC', 'Temporary Community'), ('UN', 'Unknown')], default='UN', max_length=2)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('zipcode', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coid', models.PositiveSmallIntegerField(default=0)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SystemNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_no', models.CharField(max_length=7, unique=True)),
                ('system_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.agency', to_field='system_name')),
            ],
        ),
        migrations.CreateModel(
            name='SitePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=125, unique=True)),
                ('status', models.CharField(choices=[('AB', 'Abandoned'), ('DS', 'Destroyed'), ('IA', 'Inactive'), ('AW', 'Active & Working'), ('SB', 'Stand By waiting acitvation'), ('MO', 'Monitoring')], default='SB', max_length=2)),
                ('sys_site_n', models.CharField(max_length=15, unique=True)),
                ('system_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.systemnumber')),
            ],
        ),
    ]
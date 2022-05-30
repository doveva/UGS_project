# Generated by Django 4.0.2 on 2022-02-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_name_id_points_in_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UGS_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('volume_in', models.IntegerField()),
                ('volume_out', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ugs_names')),
            ],
        ),
    ]
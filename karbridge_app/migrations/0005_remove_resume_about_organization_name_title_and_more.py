# Generated by Django 5.1.1 on 2024-10-26 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karbridge_app', '0004_rename_karfarma_organization_auther_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='about',
        ),
        migrations.AddField(
            model_name='organization_name',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='about_me',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='military_status',
            field=models.CharField(blank=True, choices=[('completed', 'پایان خدمت'), ('student_exemption', 'معافیت تحصیلی'), ('permanent_exemption', 'معافیت دائم')], max_length=25),
        ),
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.TextField(blank=True, verbose_name='آدرس'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderequestinfo',
            name='status',
            field=models.CharField(choices=[('COMFIRM', 'COMFIRM'), ('COMPLETE', 'COMPLETE'), ('OPEN', 'OPEN')], default='OPEN', max_length=20),
        ),
    ]
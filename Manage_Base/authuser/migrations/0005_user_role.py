# Generated by Django 3.2.12 on 2024-04-07 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0004_remove_userrole_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authuser.userrole'),
        ),
    ]
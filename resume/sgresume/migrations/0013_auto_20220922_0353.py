# Generated by Django 3.2.15 on 2022-09-22 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgresume', '0012_auto_20220922_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_academics', to='sgresume.geeksmodel'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_project', to='sgresume.geeksmodel'),
        ),
        migrations.AlterField(
            model_name='workexperiance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_workexp', to='sgresume.geeksmodel'),
        ),
    ]
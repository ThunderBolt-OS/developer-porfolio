# Generated by Django 4.0.4 on 2022-05-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_education_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='gpa',
            field=models.CharField(max_length=3, null=True),
        ),
    ]

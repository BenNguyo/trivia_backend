# Generated by Django 3.1.3 on 2020-11-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice2',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='choice3',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='choice4',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice1',
            field=models.CharField(default='a', max_length=100),
        ),
    ]

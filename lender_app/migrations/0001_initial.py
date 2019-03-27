# Generated by Django 2.1.7 on 2019-03-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('author', models.CharField(max_length=48)),
                ('year', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('checked-out', 'Checked-out')], default='checked-out', max_length=48)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_borrowed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

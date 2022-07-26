# Generated by Django 4.0.6 on 2022-07-25 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('grade', models.IntegerField(default=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
            ],
        ),
    ]

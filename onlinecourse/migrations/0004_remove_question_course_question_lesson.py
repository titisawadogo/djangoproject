# Generated by Django 4.0.6 on 2022-07-25 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_rename_title_question_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.AddField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson'),
            preserve_default=False,
        ),
    ]
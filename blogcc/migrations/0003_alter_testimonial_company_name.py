# Generated by Django 3.2.15 on 2022-09-15 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcc', '0002_rename_comment_approve_blogcomment_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='company_name',
            field=models.CharField(max_length=220),
        ),
    ]
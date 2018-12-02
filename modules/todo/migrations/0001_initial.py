# Generated by Django 2.1.3 on 2018-11-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=None)),
                ('is_done', models.BooleanField(default=False, null=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
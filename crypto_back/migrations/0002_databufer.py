# Generated by Django 4.1 on 2022-08-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBufer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user_strategy_choise', models.IntegerField()),
            ],
        ),
    ]
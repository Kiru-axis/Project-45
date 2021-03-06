# Generated by Django 3.2.5 on 2021-08-15 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Creditor',
                'verbose_name_plural': 'Creditors',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('shop', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='MyDebts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(blank=True)),
                ('creditor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='customers.creditor')),
            ],
            options={
                'verbose_name': 'MyDebt',
                'verbose_name_plural': 'MyDebts',
            },
        ),
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('debtor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'verbose_name': 'Debtor',
                'verbose_name_plural': 'Debtors',
            },
        ),
    ]

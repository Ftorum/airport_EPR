# Generated by Django 4.0.1 on 2022-01-31 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authy', '0001_initial'),
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('credit_card', models.CharField(blank=True, max_length=20)),
                ('code', models.CharField(editable=False, max_length=5)),
                ('total', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authy.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ticket_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flights.ticket')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authy.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authy.passenger')),
            ],
        ),
    ]
# Generated by Django 3.1 on 2020-08-11 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(unique=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(unique=True)),
                ('name', models.TextField()),
                ('nutrition_score', models.IntegerField()),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('quantity', models.TextField()),
                ('energy_100g', models.IntegerField()),
                ('energy_unit', models.TextField()),
                ('carbohydrates_100g', models.FloatField()),
                ('sugars_100g', models.FloatField()),
                ('fat_100g', models.FloatField()),
                ('saturated_fat_100g', models.FloatField()),
                ('salt_100g', models.FloatField()),
                ('sodium_100g', models.FloatField()),
                ('fiber_100g', models.FloatField()),
                ('proteins_100g', models.FloatField()),
                ('thumbnail_url', models.TextField()),
                ('categories', models.ManyToManyField(to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='product.product')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product2', to='product.product')),
            ],
            options={
                'unique_together': {('customer', 'product', 'substitute')},
            },
        ),
    ]

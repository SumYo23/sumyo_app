# Generated by Django 4.0.6 on 2023-07-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('detail', models.TextField()),
                ('image_route', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': '레시피',
                'verbose_name_plural': '레시피',
                'db_table': 'sumyo_recipe',
            },
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': '재료', 'verbose_name_plural': '재료'},
        ),
        migrations.AlterModelTable(
            name='ingredient',
            table='sumyo_ingredient',
        ),
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('method', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('ingredient', models.TextField()),
                ('recipe', models.TextField()),
                ('cook_ingredient', models.ManyToManyField(to='cook.ingredient')),
                ('cook_recipe', models.ManyToManyField(to='cook.recipe')),
            ],
            options={
                'verbose_name': '요리',
                'verbose_name_plural': '요리',
                'db_table': 'sumyo_cook',
            },
        ),
    ]

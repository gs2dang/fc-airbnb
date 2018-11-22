# Generated by Django 2.1.3 on 2018-11-21 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HouseImgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathrooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('person_capacity', models.IntegerField()),
                ('host_thumbnail_url', models.ImageField(blank=True, null=True, upload_to='pictures/host/')),
                ('host_thumbnail_url_small', models.ImageField(blank=True, null=True, upload_to='pictures/host/')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('room_name', models.CharField(max_length=200)),
                ('room_type', models.CharField(choices=[('E', 'entire'), ('P', 'private'), ('S', 'shared')], max_length=1)),
                ('price', models.IntegerField()),
                ('amenities', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='room_amenities', to='home.Amenity')),
            ],
        ),
        migrations.AddField(
            model_name='houseimgs',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_house_imgs', to='home.Room'),
        ),
        migrations.AddField(
            model_name='amenity',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Room'),
        ),
    ]
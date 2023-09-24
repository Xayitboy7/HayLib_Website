# Generated by Django 4.2.1 on 2023-05-20 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('roman', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.user')),
            ],
        ),
        migrations.CreateModel(
            name='Glav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('romani', models.CharField(max_length=50)),
                ('blogs', models.CharField(max_length=50)),
                ('still', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.user')),
            ],
        ),
        migrations.CreateModel(
            name='Resens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('resens_text', models.TextField()),
                ('lack', models.CharField(max_length=50)),
                ('roman', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.user')),
            ],
        ),
        migrations.CreateModel(
            name='Roman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.TextField()),
                ('otziv', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
                ('still', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.user')),
            ],
        ),
        migrations.CreateModel(
            name='Sobit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('sobit_text', models.TextField()),
                ('roman', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.user')),
            ],
        ),
        migrations.CreateModel(
            name='Stix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('text_stix', models.TextField()),
                ('otziv', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='story',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='story',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='story',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='story',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='story',
            name='author',
        ),
        migrations.RemoveField(
            model_name='story',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]

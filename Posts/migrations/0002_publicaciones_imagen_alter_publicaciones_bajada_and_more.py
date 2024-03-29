# Generated by Django 5.0 on 2024-03-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='foto_publicacion'),
        ),
        migrations.AlterField(
            model_name='publicaciones',
            name='bajada',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateField(max_length=30),
        ),
    ]

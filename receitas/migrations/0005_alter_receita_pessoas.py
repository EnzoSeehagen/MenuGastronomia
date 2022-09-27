# Generated by Django 4.1.1 on 2022-09-26 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0004_receita_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='pessoas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

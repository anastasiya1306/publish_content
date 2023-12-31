# Generated by Django 4.2.5 on 2023-09-22 15:24

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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Изображение')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_publication', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('payment_amount', models.IntegerField(default=0, verbose_name='Стоимость подписки')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Контент платный')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-07 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210107_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='search_value',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='list_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='search_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='search_key',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2 on 2021-06-02 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0039_alter_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='totals',
        ),
    ]
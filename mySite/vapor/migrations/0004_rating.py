# Generated by Django 5.1.1 on 2024-10-09 11:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapor', '0003_alter_game_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='ratings', to='vapor.game')),
            ],
        ),
    ]

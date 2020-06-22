# Generated by Django 2.2.4 on 2020-06-22 20:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('first_time_agent', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddIndex(
            model_name='agent',
            index=models.Index(fields=['first_name'], name='agent_first_name_idx'),
        ),
        migrations.AddIndex(
            model_name='agent',
            index=models.Index(fields=['last_name'], name='agent_last_name_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='agent',
            unique_together={('first_name', 'last_name')},
        ),
    ]

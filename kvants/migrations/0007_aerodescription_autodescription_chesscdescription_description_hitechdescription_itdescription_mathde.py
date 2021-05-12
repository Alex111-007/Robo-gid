# Generated by Django 3.2 on 2021-05-09 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvants', '0006_remove_course_choose_course_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='AeroDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='AutoDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='ChessCDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='HiTechDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='ItDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='MathDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='PromDesDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
        migrations.CreateModel(
            name='PromRoboDescription',
            fields=[
                ('description_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kvants.description')),
            ],
            bases=('kvants.description',),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 06:07
from __future__ import unicode_literals

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
            name='Attendent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('expert', 'Expert Assessor'), ('negotiator', 'Negotiator'), ('mediator', 'Mediator')], max_length=25)),
                ('blacklisted', models.BooleanField(default=False)),
                ('administrativeComment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=150)),
                ('issueDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20, verbose_name='Year you have taken the course')),
                ('instructor', models.CharField(blank=True, max_length=70, null=True)),
                ('institution', models.CharField(blank=True, max_length=100, null=True)),
                ('learnings', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(verbose_name='Years of Experience in this role')),
                ('cases', models.IntegerField(verbose_name='Number of engagements worked')),
                ('description', models.TextField(verbose_name='Brief outline of the relevant professional background')),
                ('priorClients', models.TextField(verbose_name='What key clients did you work with in this role?')),
                ('placesWorked', models.TextField(verbose_name='Where did you work from/at?')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=100, verbose_name='Name of Firm or Instituation')),
                ('year', models.CharField(max_length=4)),
                ('duration', models.CharField(max_length=10, verbose_name='Duration of your Practice')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=5000)),
                ('country', models.CharField(max_length=100)),
                ('profileImg', models.ImageField(blank=True, upload_to='/profileImg/')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('attendent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Attendent')),
            ],
            bases=('UserManagement.attendent',),
        ),
        migrations.CreateModel(
            name='ExpertProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Profile')),
                ('slogan', models.TextField(blank=True, max_length=500)),
            ],
            bases=('UserManagement.profile',),
        ),
        migrations.CreateModel(
            name='MediationExperience',
            fields=[
                ('experience_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Experience')),
                ('profession', models.IntegerField(choices=[(1, 'Practicing Mediator'), (2, 'Mediation Trainer'), (3, 'Judged Mediation Competitions'), (4, 'NO prior Experience')])),
            ],
            bases=('UserManagement.experience',),
        ),
        migrations.CreateModel(
            name='MediationPractice',
            fields=[
                ('internship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Internship')),
            ],
            bases=('UserManagement.internship',),
        ),
        migrations.CreateModel(
            name='NegotiationExperience',
            fields=[
                ('experience_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Experience')),
                ('profession', models.IntegerField(choices=[(1, 'Practicing Negotiator'), (2, 'Negotiaton Trainer'), (3, 'Judged Negotiaton Competitions'), (4, 'NO prior Experience')])),
            ],
            bases=('UserManagement.experience',),
        ),
        migrations.CreateModel(
            name='NegotiationPractice',
            fields=[
                ('internship_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Internship')),
            ],
            bases=('UserManagement.internship',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('attendent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Attendent')),
                ('shifts', models.CharField(max_length=200)),
            ],
            bases=('UserManagement.attendent',),
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Profile')),
                ('slogan', models.CharField(max_length=250, verbose_name='Your favorite quote up to 250 characters')),
                ('phoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('Twitter', models.URLField(blank=True, null=True, verbose_name='Your Twitter Account')),
                ('Facebook', models.URLField(blank=True, null=True, verbose_name='Link to your Facebook Page')),
                ('Blog', models.URLField(blank=True, null=True, verbose_name='Link to a related professional Blog')),
                ('mediation_courses', models.ManyToManyField(related_name='medCourses', to='UserManagement.Course')),
                ('negotiation_courses', models.ManyToManyField(related_name='negCourses', to='UserManagement.Course')),
            ],
            bases=('UserManagement.profile',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('attendent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Attendent')),
                ('university', models.CharField(max_length=100)),
            ],
            bases=('UserManagement.attendent',),
        ),
        migrations.CreateModel(
            name='TeamProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserManagement.Profile')),
                ('university', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('UserManagement.profile',),
        ),
        migrations.AddField(
            model_name='attendent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='attendent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Attendent'),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='certifications',
            field=models.ManyToManyField(blank=True, to='UserManagement.Certification'),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='mediation_experience',
            field=models.ManyToManyField(blank=True, related_name='mediation_experience', to='UserManagement.MediationExperience'),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='negotiation_experience',
            field=models.ManyToManyField(blank=True, related_name='negotiation_experience', to='UserManagement.NegotiationExperience'),
        ),
    ]

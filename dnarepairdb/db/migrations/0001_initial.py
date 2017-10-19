# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-19 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=30)),
                ('research_description', models.TextField(null=True)),
                ('webpage_link', models.TextField(null=True)),
                ('image_link', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flybase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flybase_id', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ncbi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geneid', models.CharField(max_length=15)),
                ('gi', models.CharField(max_length=15)),
                ('genebank', models.CharField(max_length=20)),
                ('refseq', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=3)),
                ('specific_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ortholog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20, null=True)),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Gene')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Organism')),
            ],
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdb_id', models.CharField(max_length=15)),
                ('title', models.TextField(null=True)),
                ('ortholog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Ortholog')),
            ],
        ),
        migrations.CreateModel(
            name='Uniprot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniprot_id', models.CharField(max_length=15)),
                ('ortholog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Ortholog')),
            ],
        ),
        migrations.CreateModel(
            name='Wormdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wormdb_id', models.CharField(max_length=15)),
                ('ortholog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Ortholog')),
            ],
        ),
        migrations.CreateModel(
            name='Yeastdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yeastdb_id', models.CharField(max_length=15)),
                ('ortholog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Ortholog')),
            ],
        ),
        migrations.AddField(
            model_name='ncbi',
            name='ortholog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Ortholog'),
        ),
        migrations.AddField(
            model_name='gene',
            name='pathway',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Pathway'),
        ),
        migrations.AddField(
            model_name='flybase',
            name='ortholog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Ortholog'),
        ),
    ]
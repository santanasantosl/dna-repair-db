# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pathway(models.Model):

    name = models.CharField(max_length=40, null=False)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name

class Gene(models.Model):

    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pathway = models.ForeignKey(Pathway)

    def __unicode__(self):
        return self.symbol

class Organism(models.Model):

    abbreviation = models.CharField(max_length=3, null=False)
    specific_name = models.CharField(max_length=30, null=False)

    def __unicode__(self):
        return self.abbreviation

class Ortholog(models.Model):

    gene = models.ForeignKey(Gene, null=False)
    organism = models.ForeignKey(Organism, null=False)
    symbol = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.gene


class Uniprot(models.Model):

    uniprot_id = models.CharField(max_length=15)
    ortholog = models.ForeignKey(Ortholog, null=True)

    def __unicode__(self):
        return self.uniprot_id


class Pdb(models.Model):

    ortholog = models.ForeignKey(Ortholog, null=False)
    pdb_id = models.CharField(max_length=15, null=False)
    title = models.TextField(null=True)

    def __unicode__(self):
        return self.pdb_id


class Ncbi(models.Model):

    geneid = models.CharField(max_length=15, null=False)
    gi = models.CharField(max_length=15, null=False)
    genebank = models.CharField(max_length=20, null=False)
    refseq = models.CharField(max_length=15, null=False)
    ortholog = models.ForeignKey(Ortholog, null=True)

    def __unicode__(self):
        return self.geneid


class Yeastdb(models.Model):

    yeastdb_id = models.CharField(max_length=15)
    ortholog = models.ForeignKey(Ortholog, null=True)

    def __unicode__(self):
        return self.yeastdb_id


class Flybase(models.Model):

    flybase_id = models.CharField(max_length=15)
    ortholog = models.ForeignKey(Ortholog, null=True)

    def __unicode__(self):
        return self.flybase_id


class Wormdb(models.Model):

    wormdb_id = models.CharField(max_length=15)
    ortholog = models.ForeignKey(Ortholog, null=True)

    def __unicode__(self):
        return self.wormdb_id


class Faculty(models.Model):

    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=30, null=False)
    research_description = models.TextField(null=True)
    webpage_link = models.TextField(null=True)
    image_link = models.TextField(null=True)

    def __unicode__(self):
        return self.first_name
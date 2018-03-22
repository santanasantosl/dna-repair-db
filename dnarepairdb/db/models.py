# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Organism(models.Model):

    abbreviation = models.CharField(max_length=3, null=False)
    specific_name = models.CharField(max_length=30, null=False)
    common_name = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.abbreviation


class Pathway(models.Model):

    name = models.CharField(max_length=40, null=False)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name


class Gene(models.Model):

    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    organism = models.ForeignKey(Organism, null=True)

    def __unicode__(self):
        return self.symbol


class GenePathway(models.Model):

    gene = models.ForeignKey(Gene)
    pathway = models.ForeignKey(Pathway)


class Ortholog(models.Model):

    gene = models.ForeignKey(Gene, null=False)
    organism = models.ForeignKey(Organism, null=False)
    symbol = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.gene.symbol


class Uniprot(models.Model):

    uniprot_id = models.CharField(max_length=15)
    ortholog = models.ForeignKey(Ortholog, null=True)

    def __unicode__(self):
        return self.uniprot_id


class Pdb(models.Model):

    ortholog = models.ForeignKey(Ortholog, null=False)
    pdb_id = models.CharField(max_length=15, null=False)
    title = models.TextField(null=True)
    pdb_link = models.TextField(null=True)

    def __unicode__(self):
        return self.pdb_id


class Ncbi(models.Model):

    geneid = models.CharField(max_length=15, null=True, blank=True, default=None)
    gi = models.CharField(max_length=15, null=True, blank=True, default=None)
    genebank = models.CharField(max_length=20, null=True, blank=True, default=None)
    refseq = models.CharField(max_length=15, null=True, blank=True, default=None)
    ortholog = models.ForeignKey(Ortholog, null=False, default=None)

    def __unicode__(self):
        if self.geneid is not None:
            return self.geneid
        else:
            return self.ortholog.gene.symbol


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
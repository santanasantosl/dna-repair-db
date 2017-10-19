# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)


def pathways(request, pathwayid):
    pathway_rec = Pathway.objects.filter(id=pathwayid).get()
    genes_inside_pathway = Gene.objects.filter(pathway=pathwayid)
    organism = Organism.objects.all()

    context = locals()
    template = 'pathways.html'
    return render(request, template, {'current_pathway': pathway_rec,
                                      'genes_inside_pathway': genes_inside_pathway,
                                      'organisms': organism})

def orthologs(request):
    template = 'orthologs.html'
    gene_rec = Gene.objects.all()
    organism_rec = Organism.objects.all()
    return render(request, template, {
        'organisms': organism_rec})

    # ortholog_table = dict()
    #
    # for gene in gene_rec:
    #     for organism in organism_rec:
    #
    #         #ortholog_table[gene.symbol] = organism.abbreviation
    #         current_ortholog_rec = Ortholog.objects.filter(organism_id=organism.id, gene_id=gene.id)
    #         if current_ortholog_rec.count() > 0:
    #
    #             if ortholog_table.has_key(gene.symbol):
    #                 ortholog_table[gene.symbol][organism.abbreviation] = current_ortholog_rec.symbol
    #
    #             else:
    #                 ortholog_table[gene.symbol] = dict()
    #                 ortholog_table[gene.symbol][organism.abbreviation] = current_ortholog_rec.symbol
    #         elif current_ortholog_rec.count() == 0:
    #             if ortholog_table.has_key(gene.symbol):
    #                 ortholog_table[gene.symbol][organism.abbreviation] = ""
    #
    #             else:
    #                 ortholog_table[gene.symbol] = list()
    #                 ortholog_table[gene.symbol][organism.abbreviation] = ""
    #
    #
    # return render(request, template, {
    #     'organisms': organism_rec, 'ortholog_table': ortholog_table})


def faculty(request):
    context = locals()
    template = 'faculty.html'

    faculty_rec = Faculty.objects.all()

    return render(request, template, {
        'faculty': faculty_rec})
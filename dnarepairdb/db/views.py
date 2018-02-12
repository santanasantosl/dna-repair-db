# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pathway, Gene, Organism, Faculty, GenePathway, Ortholog, Ncbi, Uniprot, Pdb, Wormdb, Flybase, Yeastdb

# Create your views here.


def home(request):
    context = locals()
    template = 'home.html'
    organisms = Organism.objects.all().values_list('specific_name', flat=True)

    organism_list = ", ".join(list(organisms))

    return render(request, template, {'organism_list': organism_list})


def all_pathways(request, pathwayid):
    context = locals()
    template = 'home.html'
    organisms = Organism.objects.all().values_list('specific_name', flat=True)

    organism_list = ", ".join(list(organisms))

    return render(request, template, {'organism_list': organism_list})


def pathways(request, pathwayid):

    pathway_data = []

    pathway_rec = Pathway.objects.filter(id=pathwayid).get()
    genes_inside_pathway = GenePathway.objects.filter(pathway=pathwayid)
    organisms = Organism.objects.all()

    for gene_pathway in genes_inside_pathway:
        current_gene = gene_pathway.gene

        gene_dict = dict()
        for organism in organisms:
            try:
                ortholog = Ortholog.objects.get(gene=current_gene, organism=organism)
                gene_dict[organism.abbreviation] = ortholog
            except:
                gene_dict[organism.abbreviation] = None
        pathway_data.append(gene_dict)

    template = 'pathways.html'
    return render(request, template, {'current_pathway': pathway_rec,
                                      'genes_inside_pathway': genes_inside_pathway,
                                      'pathway_data': pathway_data,
                                      'organisms': organisms})


def all_orthologs(request, organismid):

    context = locals()
    template = 'all_orthologs.html'

    data = []

    organism_obj = Organism.objects.get(id=organismid)
    orthologs = Ortholog.objects.filter(organism=organism_obj)
    for ortholog in orthologs:
        gene_pathway = GenePathway.objects.get(gene=ortholog.gene)
        pathway = gene_pathway.pathway
        result_dict = {'ortholog':ortholog, 'pathway': pathway}
        data.append(result_dict)

    return render(request, template, {'data':data, 'organism': organism_obj})


def orthologs(request, orthologid):

    template = 'orthologs.html'

    ortholog_obj = Ortholog.objects.get(id=orthologid)
    gene_obj = ortholog_obj.gene
    organism_obj = ortholog_obj.organism

    annotation_data = {}

    # Get NCBI
    try:
        ncbi = Ncbi.objects.get(ortholog=ortholog_obj)
        annotation_data['ncbi'] = ncbi
    except:
        pass

    # Get Uniprot
    try:
        uniprot = Uniprot.objects.get(ortholog=ortholog_obj)
        annotation_data['uniprot'] = uniprot
    except:
        pass

    # Get PDB

    pdb = Pdb.objects.filter(ortholog=ortholog_obj)
    annotation_data['pdb'] = pdb

    # Get wormdb
    try:
        wormdb = Wormdb.objects.get(ortholog=ortholog_obj)
        annotation_data['wormdb'] = wormdb
    except:
        pass

    # Get Flybase
    try:
        flybase = Flybase.objects.get(ortholog=ortholog_obj)
        annotation_data['flybase'] = flybase
    except:
        pass

    # Get Yeastdb
    try:
        yeastdb = Yeastdb.objects.get(ortholog=ortholog_obj)
        annotation_data['yeastdb'] = yeastdb
    except:
        pass

    # Get remaining orthologs
    remaining_organisms = Organism.objects.exclude(id=organism_obj.id)

    orthologs_data = dict()
    for current_organism in remaining_organisms:
        try:
            current_ortholog = Ortholog.objects.get(gene=gene_obj, organism=current_organism)
            orthologs_data[current_organism.abbreviation] = current_ortholog
        except:
            pass

    sorted_orthologs = orthologs_data.keys()
    sorted_orthologs.sort()

    sorted_ortholog_data = list()
    for ortholog in sorted_orthologs:
        sorted_ortholog_data.append(orthologs_data[ortholog])


    return render(request, template, {
        'orthologs_data': sorted_ortholog_data,
        'ortholog_obj': ortholog_obj,
        'annotation_data': annotation_data,})


def faculty(request):
    context = locals()
    template = 'faculty.html'

    faculty_rec = Faculty.objects.all()

    return render(request, template, {
        'faculty': faculty_rec})
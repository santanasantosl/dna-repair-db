import os
import re
import json
import django
django.setup()
from django.conf import settings

from db.models import Gene, Pathway, GenePathway, Organism, Ortholog, Pdb, Uniprot, Ncbi


def load_data(json_file):

    json_data = json.load(open(json_file))
    json_data_list = json_data[json_data.keys()[0]]

    for entry in json_data_list:

        organisms = ['hsa', 'mmu', 'dme', 'ath', 'cel', 'sce', 'spo']

        hsa_obj = Organism.objects.get(abbreviation='hsa')
        gene_symbol = entry['hsaName']
        # Add gene
        try:
            gene_obj = Gene.objects.get(symbol=gene_symbol, organism=hsa_obj)
        except:
            gene_obj = Gene(symbol=gene_symbol, organism=hsa_obj)
            gene_obj.save()

        #### Add orthologs

        # HSA
        hsa_ortholog = add_or_get_orthologs(organism_abbreviation='hsa', gene_obj=gene_obj, symbol=gene_symbol)

        # MMU
        mmu_ortholog = add_or_get_orthologs(organism_abbreviation='mmu', gene_obj=gene_obj, symbol=entry['mmuName'])

        # DME
        dme_ortholog = add_or_get_orthologs(organism_abbreviation='dme', gene_obj=gene_obj, symbol=entry['dmeName'])

        # ATH
        ath_ortholog = add_or_get_orthologs(organism_abbreviation='ath', gene_obj=gene_obj, symbol=entry['athName'])

        # CEL
        cel_ortholog = add_or_get_orthologs(organism_abbreviation='cel', gene_obj=gene_obj, symbol=entry['celWormPD'])

        # SCE
        sce_ortholog = add_or_get_orthologs(organism_abbreviation='sce', gene_obj=gene_obj, symbol=entry['sceName'])

        # SPO
        spo_ortholog = add_or_get_orthologs(organism_abbreviation='spo', gene_obj=gene_obj, symbol=entry['spoName'])

        pathway = entry['category']
        try:
            pathway_obj = Pathway.objects.get(name=pathway)
        except:
            pathway_obj = Pathway(name=pathway)
            pathway_obj.save()

        #### Add genes to pathways
        try:
            gene_pathway_obj = GenePathway.objects.get(gene=gene_obj, pathway=pathway_obj)
        except:
            gene_pathway_obj = GenePathway(gene=gene_obj, pathway=pathway_obj)
            gene_pathway_obj.save()


        #### Add PDB
        pdbs = str(entry['PDB']).split(' ')
        for pdb in pdbs:
             if pdb != '':
                 try:
                     pdb_obj = Pdb.objects.get(pdb_id=pdb)
                 except:
                     pdb_obj = Pdb(pdb_id=pdb, ortholog=hsa_ortholog)
                     pdb_obj.save()

        uniprot_objs = add_or_get_uniprot(entry, organisms, gene_obj)
        ncbi_objs = add_or_get_ncbi(entry, organisms, gene_obj)


def add_or_get_ncbi(data, organisms, gene_obj):

    ncbi_objs = []
    for organism in organisms:
        gi_key = organism + 'Gi'
        geneid_key = organism + 'GeneID'
        genebank_key = organism + 'GenBank'
        refseq = organism + 'Acc'

        ortholog_obj = None
        try:
            ortholog_obj = Ortholog.objects.get(gene=gene_obj, organism__abbreviation=organism)
        except:
            pass
        if ortholog_obj:

            current_data = {}
            if data.has_key(gi_key):
                if data[gi_key] != '':
                    current_data['gi'] = data[gi_key]
            if data.has_key(geneid_key):
                if data[geneid_key] != '':
                    current_data['geneid'] = data[geneid_key]
            if data.has_key(genebank_key):
                if data[genebank_key] != '':
                    current_data['genebank'] = data[genebank_key]
            if data.has_key(refseq):
                if data[refseq] != '':
                    current_data['refseq'] = data[refseq]
            try:
                ncbi_obj = Ncbi.objects.get(ortholog=ortholog_obj)
                ncbi_objs.append(ncbi_obj)

            except:
                ncbi_obj = Ncbi(ortholog=ortholog_obj)
                ncbi_obj.save()

                if current_data.has_key('gi'):
                    ncbi_obj.gi = current_data['gi']
                    ncbi_obj.save(update_fields=['gi',])
                if current_data.has_key('genebank'):
                    ncbi_obj.genebank = current_data['genebank']
                    ncbi_obj.save(update_fields=['genebank', ])
                if current_data.has_key('geneid'):
                    ncbi_obj.geneid = current_data['geneid']
                    ncbi_obj.save(update_fields=['geneid', ])
                if current_data.has_key('refseq'):
                    ncbi_obj.refseq = current_data['refseq']
                    ncbi_obj.save(update_fields=['refseq', ])
                ncbi_objs.append(ncbi_obj)
    return ncbi_objs


def add_or_get_uniprot(data, organisms, gene_obj):

    uniprot_objs = []

    for organism in organisms:
        if data.has_key(organism + 'Uniprot'):
            if data[organism + 'Uniprot'] != '':
                fields = data[organism + 'Uniprot'].split(' ')
                for entry in fields:
                    if entry != '':
                        if re.search('#', entry):
                            fields = entry.split('#')
                            for field in fields:
                                ortholog_obj = None
                                try:
                                    ortholog_obj = Ortholog.objects.get(gene=gene_obj, organism__abbreviation=organism)
                                except:
                                    pass
                                if ortholog_obj:
                                    try:
                                        uniprot_obj = Uniprot.objects.get(uniprot_id=field, ortholog=ortholog_obj)
                                    except:
                                        uniprot_obj = Uniprot(uniprot_id=field, ortholog=ortholog_obj)
                                        uniprot_obj.save()
                                    uniprot_objs.append(uniprot_obj)
                        else:
                            ortholog_obj = None
                            try:
                                ortholog_obj = Ortholog.objects.get(gene=gene_obj, organism__abbreviation=organism)
                            except:
                                pass
                            if ortholog_obj:
                                try:
                                    uniprot_obj = Uniprot.objects.get(uniprot_id=entry, ortholog=ortholog_obj)
                                except:
                                    uniprot_obj = Uniprot(uniprot_id=entry, ortholog=ortholog_obj)
                                    uniprot_obj.save()
                                uniprot_objs.append(uniprot_obj)
    return uniprot_objs


def add_or_get_orthologs(organism_abbreviation, gene_obj, symbol):

    ortholog_obj = None
    if symbol != '':
        organism_obj = Organism.objects.get(abbreviation=organism_abbreviation)

        try:
            ortholog_obj = Ortholog.objects.get(gene=gene_obj, organism=organism_obj, symbol=symbol)
        except:
            ortholog_obj = Ortholog(gene=gene_obj, organism=organism_obj, symbol=symbol)
            ortholog_obj.save()

        return ortholog_obj
    return ortholog_obj


if __name__ == "__main__":

    json_file = os.path.join(settings.MEDIA_ROOT, 'repair.json')
    load_data(json_file)
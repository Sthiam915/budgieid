import numpy as np

MUTATION_TRAITS = {
    'color_base':['yellow', 'white'],
    'dark_factor':'',
    'violet_factor':'',
    'grey_factor':'',
    'dilution':['greywing', 'clearwing', 'dilute'],
    'albino':'',
    'lutino':'',
    'yellowface':['type_1', 'type_2'],
    'cinnamon':'',
    'opaline':'',
    'spangle':'',
    'dominant_pied':'',
    'recessive_pied':'',
    'clearflight_pied':'',
    'clearbody':'',
    'fallow':'',
    
}

class Allele:
    def __init__(self, name='', sex_linked=False, part_affected=None, genotype=None):
        self.name = name
        self.sex_linked = sex_linked
        self.part_affected = part_affected
        self.genotype = genotype
    
    def cross(self, allele_2):
        if (self.name, self.sex_linked, self.part_affected) != (allele_2.name, allele_2.sex_linked, allele_2.part_affected):
            return None
        
        args = {'name':self.name, 'sex_linked':self.sex_linked, 'part_affected':self.part_affected}
        return [Allele(**args, genotype=[self.genotype[1 // 2], allele_2.genotype[i % 2]]) for i in range(4)]


class Bird_Alleles:
    pass



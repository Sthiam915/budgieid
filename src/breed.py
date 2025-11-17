import numpy as np

MUTATION_TRAITS = {
    'color':['yellow', 'white'],
    'dark_factor':'',
    'violet_factor':'',
    'grey_factor':'',
    'dilution':['greywing', 'clearwing', 'dilute'], # sp
    'ino':'',
    'yellowface':['type_1', 'type_2'], # sp
    'cinnamon':'',
    'opaline':'',
    'spangle':'',
    'dominant_pied':'',
    'recessive_pied':'',
    'clearflight_pied':'',
    'clearbody':'',
    'fallow':'',
    
}

class Genotype:
    def __init__(self, allele_1, allele_2):
        
        if not allele_2 or allele_1 < allele_2:
            self.allele_1 = allele_1
            self.allele_2 = allele_2
        else:
            self.allele_1 = allele_2
            self.allele_2 = allele_1
    def __repr__(self):
        return ''.join([str(self.allele_1), '' if not self.allele_2 else self.allele_2])
    def __str__(self):
        return ''.join([str(self.allele_1), '' if not self.allele_2 else self.allele_2])
    def __eq__(self, other):
        if self.allele_1 == other.allele_1 and self.allele_2 == other.allele_2:
            return True
        if self.allele_1 == other.allele_2 and other.allele_1 == self.allele_2:
            return True
        return False
    def __hash__(self):
        return ''.join(sorted([self.allele_1, self.allele_2])).__hash__() if self.allele_2 else self.allele_1.__hash__()
class Allele:
    def __init__(self, name='', sex = '',sex_linked=False, parts_affected=None, genotype:Genotype=None):
        if not name in MUTATION_TRAITS:
            raise Exception("Invalid mutation name")
        if not parts_affected.issubset({'face', 'body', 'wings'}):
            raise Exception("parts_affected must be 'face', 'body', or 'wings")
        if not Genotype in type(genotype).mro():
            raise Exception("genotype must be of type Genotype")
        # if not sex in {'m', 'f'}:
        #     raise Exception('Sex must be M or F')
        self.sex = sex
        self.name = name
        self.sex_linked = sex_linked
        self.parts_affected = parts_affected
        self.genotype = genotype
    
    def cross(self, allele_2):
        if (self.name, self.sex_linked, self.parts_affected) != (allele_2.name, allele_2.sex_linked, allele_2.parts_affected):
            return None
        
        if not self.sex_linked:
            # return all unique combinations
            args = {'name':self.name,  'sex_linked':self.sex_linked, 'parts_affected':self.parts_affected}
            ret = []
            
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_1, allele_2.genotype.allele_1), sex='m'))
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_1, allele_2.genotype.allele_2), sex='m'))
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_2, allele_2.genotype.allele_1), sex='m'))
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_2, allele_2.genotype.allele_2), sex='m'))
            
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_1, allele_2.genotype.allele_1), sex='f'))
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_1, allele_2.genotype.allele_2), sex='f'))
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_2, allele_2.genotype.allele_1), sex='f'))
            ret.append(Allele(**args, genotype=Genotype(self.genotype.allele_2, allele_2.genotype.allele_2), sex='f'))
            return list(set(ret))
        else:
            # cross for sex-linked alleles
            args = {'name':self.name, 'sex_linked':self.sex_linked, 'parts_affected':self.parts_affected}
            ret = []
            if self.sex == 'f':
                f_allele = self
                m_allele = allele_2
            elif self.sex == 'm':
                f_allele = allele_2
                m_allele = self
            
            # female offspring

            ret.append(Allele(**args, genotype=Genotype(m_allele.genotype.allele_1, None), sex='f'))
            ret.append(Allele(**args, genotype=Genotype(m_allele.genotype.allele_2, None), sex='f'))

            # male offspring
            ret.append(Allele(**args, genotype=Genotype(m_allele.genotype.allele_1, f_allele.genotype.allele_1), sex='m'))
            ret.append(Allele(**args, genotype=Genotype(m_allele.genotype.allele_2, f_allele.genotype.allele_1), sex='m'))

            return list(set(ret))
    def __eq__(self, other):
        if not type(other) == Allele:
            raise TypeError("Can only compare Allele with Allele")
        
        return self.name == other.name and self.sex_linked == other.sex_linked and \
            self.parts_affected == other.parts_affected and self.genotype == other.genotype and \
            self.sex == other.sex
    def __hash__(self):
        return (self.name + str(self.sex_linked) + ''.join(sorted(self.parts_affected)) + str(self.genotype) + self.sex).__hash__()

class Bird:
    def __init__(self, sex=None,
                 color:Allele=None, dark_factor:Allele=None, violet_factor:Allele=None,
                 grey_factor:Allele=None, ino:Allele=None, cinnamon:Allele=None, opaline:Allele=None,
                 spangle:Allele=None, dominant_pied:Allele=None, recessive_pied:Allele=None,
                 clearflight_pied:Allele=None, clearbody:Allele=None, fallow:Allele=None):
        if not sex in {'m', 'f'}:
            raise Exception('Sex must be "m" or "f"')
        self.sex = sex

        self.color:Allele = color
        self.dark_factor:Allele = dark_factor
        self.violet_factor:Allele = violet_factor
        self.grey_factor:Allele = grey_factor
        self.ino:Allele = ino
        self.cinnamon:Allele = cinnamon
        self.opaline:Allele = opaline
        self.spangle:Allele = spangle
        self.dominant_pied:Allele = dominant_pied
        self.recessive_pied:Allele = recessive_pied
        self.clearflight_pied:Allele = clearflight_pied
        self.clearbody:Allele = clearbody
        self.fallow:Allele = fallow

    def breed(self, other):
        if not type(other) == Bird:
            raise TypeError("Argument must be another bird")

        color_combinations = self.color.cross(other.color)
        dark_factor_combinations = self.dark_factor.cross(other.dark_factor)
        violet_factor_combinations = self.violet_factor.cross(other.violet_factor)
        grey_factor_combinations = self.grey_factor.cross(other.grey_factor)
        ino_combinations = self.ino.cross(other.ino)
        cinnamon_combinations = self.cinnamon.cross(other.cinnamon)
        opaline_combinations = self.opaline.cross(other.opaline)
        spangle_combinations = self.spangle.cross(other.spangle)
        dominant_pied_combinations = self.dominant_pied.cross(other.dominant_pied)
        recessive_pied_combinations = self.recessive_pied.cross(other.recessive_pied)
        clearflight_pied_combinations = self.clearflight_pied.cross(other.clearflight_pied)
        clearbody_combinations = self.clearbody.cross(other.clearbody)
        fallow_combinations = self.fallow.cross(other.fallow)
        combinations = []
        
        
    
        for sex in {'m', 'f'}:
            for color in [i for i in color_combinations if i.sex == sex]:
                for dark_factor in [i for i in dark_factor_combinations if i.sex == sex]:
                    for violet_factor in [i for i in violet_factor_combinations if i.sex == sex]:
                        for grey_factor in [i for i in grey_factor_combinations if i.sex == sex]:
                            for ino in [i for i in ino_combinations if i.sex == sex]:
                                for cinnamon in [i for i in cinnamon_combinations if i.sex == sex]:
                                    for opaline in [i for i in opaline_combinations if i.sex == sex]:
                                        for spangle in [i for i in spangle_combinations if i.sex == sex]:
                                            for dominant_pied in [i for i in dominant_pied_combinations if i.sex == sex]:
                                                for recessive_pied in [i for i in recessive_pied_combinations if i.sex == sex]:
                                                    for clearflight_pied in [i for i in clearflight_pied_combinations if i.sex == sex]:
                                                        for clearbody in [i for i in clearbody_combinations if i.sex == sex]:
                                                            for fallow in [i for i in fallow_combinations if i.sex == sex]:
                                                                b = Bird(sex=sex,
                                                                         color=color, dark_factor=dark_factor, violet_factor=violet_factor,
                                                                         grey_factor=grey_factor, ino=ino, cinnamon=cinnamon, opaline=opaline,
                                                                         spangle=spangle, dominant_pied=dominant_pied, recessive_pied=recessive_pied,
                                                                         clearflight_pied=clearflight_pied, clearbody=clearbody, fallow=fallow)
                                                                if not b in combinations:
                                                                    combinations.append(b)
                                                                    
        return combinations
    def __str__(self):
        ret = f""
        ret += f"Sex: {self.sex}\n"
        ret += f"Color: {str(self.color.genotype)}\n"       
        ret += f"Dark Factor: {str(self.dark_factor.genotype)}\n"
        ret += f"Violet Factor: {str(self.violet_factor.genotype)}\n"
        ret += f"Grey Factor: {str(self.grey_factor.genotype)}\n"
        ret += f"Ino: {str(self.ino.genotype)}\n"
        ret += f"Cinnamon: {str(self.cinnamon.genotype)}\n"
        ret += f"Opaline: {str(self.opaline.genotype)}\n"
        ret += f"Spangle: {str(self.spangle.genotype)}\n"
        ret += f"Dominant Pied: {str(self.dominant_pied.genotype)}\n"
        ret += f"Recessive Pied: {str(self.recessive_pied.genotype)}\n"
        ret += f"Clearflight Pied: {str(self.clearflight_pied.genotype)}\n"
        ret += f"Clearbody: {str(self.clearbody.genotype)}\n"
        ret += f"Fallow: {str(self.fallow.genotype)}\n"
        return ret
    def __repr__(self):
        ret = f""
        ret += f"Sex: {self.sex}\n"
        ret += f"Color: {str(self.color.genotype)}\n"       
        ret += f"Dark Factor: {str(self.dark_factor.genotype)}\n"
        ret += f"Violet Factor: {str(self.violet_factor.genotype)}\n"
        ret += f"Grey Factor: {str(self.grey_factor.genotype)}\n"
        ret += f"Ino: {str(self.ino.genotype)}\n"
        ret += f"Cinnamon: {str(self.cinnamon.genotype)}\n"
        ret += f"Opaline: {str(self.opaline.genotype)}\n"
        ret += f"Spangle: {str(self.spangle.genotype)}\n"
        ret += f"Dominant Pied: {str(self.dominant_pied.genotype)}\n"
        ret += f"Recessive Pied: {str(self.recessive_pied.genotype)}\n"
        ret += f"Clearflight Pied: {str(self.clearflight_pied.genotype)}\n"
        ret += f"Clearbody: {str(self.clearbody.genotype)}\n"
        ret += f"Fallow: {str(self.fallow.genotype)}\n"
        return ret
    def __eq__(self, other):
        if not type(other) == Bird:
            raise TypeError("Can only compare Bird with Bird")
        # sex and all mutations must be equal
        return self.color == other.color and \
            self.sex == other.sex and self.dark_factor == other.dark_factor and \
            self.violet_factor == other.violet_factor and self.grey_factor == other.grey_factor and \
            self.ino == other.ino and self.cinnamon == other.cinnamon and self.opaline == other.opaline and \
            self.spangle == other.spangle and self.dominant_pied == other.dominant_pied and \
            self.recessive_pied == other.recessive_pied and self.clearflight_pied == other.clearflight_pied and \
            self.clearbody == other.clearbody and self.fallow == other.fallow
            
        
if __name__ == '__main__':
    
    
    # test cases    
    tc_allele_1 = Allele('color', sex='m', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D'))
    tc_allele_2 = Allele('color', sex='f', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D'))

    res = tc_allele_1.cross(tc_allele_2)
    print(res)
    print([i.genotype for i in res])

    tc_1_male = {
        'sex':'m',
        'color':Allele('color', sex='m', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'dark_factor':Allele('dark_factor', sex='m', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'violet_factor':Allele('violet_factor', sex='m', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'grey_factor':Allele('grey_factor', sex='m', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'ino':Allele('ino', sex='m', sex_linked=True, parts_affected={'body'}, genotype=Genotype('D','D')),
        'cinnamon':Allele('cinnamon', sex='m', sex_linked=True, parts_affected={'body'}, genotype=Genotype('D','D')),
        'opaline':Allele('opaline', sex='m', sex_linked=False, parts_affected={'body', 'wings'}, genotype=Genotype('D','D')),
        'spangle':Allele('spangle', sex='m', sex_linked=False, parts_affected={'body', 'wings'}, genotype=Genotype('D','D')),
        'dominant_pied':Allele('dominant_pied', sex='m', sex_linked=False, parts_affected={'body', 'wings', 'face'}, genotype=Genotype('D','D')),
        'recessive_pied':Allele('recessive_pied', sex='m', sex_linked=False, parts_affected={'body', 'wings', 'face'}, genotype=Genotype('D','D')),
        'clearflight_pied':Allele('clearflight_pied', sex='m', sex_linked=False, parts_affected={'body', 'wings', 'face'}, genotype=Genotype('D','D')),
        'clearbody':Allele('clearbody', sex='m', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'fallow':Allele('fallow', sex='m', sex_linked=False, parts_affected={'body', 'face', 'wings'}, genotype=Genotype('D','D')),
    }

    tc_1_female = {
        'sex':'f',
        'color':Allele('color', sex='f', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'dark_factor':Allele('dark_factor', sex='f', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'violet_factor':Allele('violet_factor', sex='f', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'grey_factor':Allele('grey_factor', sex='f', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'ino':Allele('ino', sex='f', sex_linked=True, parts_affected={'body'}, genotype=Genotype('D',None)),
        'cinnamon':Allele('cinnamon', sex='f', sex_linked=True, parts_affected={'body'}, genotype=Genotype('D',None)),
        'opaline':Allele('opaline', sex='f', sex_linked=False, parts_affected={'body', 'wings'}, genotype=Genotype('D','D')),
        'spangle':Allele('spangle', sex='f', sex_linked=False, parts_affected={'body', 'wings'}, genotype=Genotype('D','D')),
        'dominant_pied':Allele('dominant_pied', sex='f', sex_linked=False, parts_affected={'body', 'wings', 'face'}, genotype=Genotype('D','D')),
        'recessive_pied':Allele('recessive_pied', sex='f', sex_linked=False, parts_affected={'body', 'wings', 'face'}, genotype=Genotype('D','D')),
        'clearflight_pied':Allele('clearflight_pied', sex='f', sex_linked=False, parts_affected={'body', 'wings', 'face'}, genotype=Genotype('D','D')),
        'clearbody':Allele('clearbody', sex='f', sex_linked=False, parts_affected={'body'}, genotype=Genotype('D','D')),
        'fallow':Allele('fallow', sex='f', sex_linked=False, parts_affected={'body', 'face', 'wings'}, genotype=Genotype('D','D')),
    }

    bird_1 = Bird(**tc_1_male)
    bird_2 = Bird(**tc_1_female)
    offspring = bird_1.breed(bird_2)


    for i in offspring:
        print(i)
        print('-----')

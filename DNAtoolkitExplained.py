#DNA toolkit creation 
import collections
from sequences import *


# now need a 'validate sequence' fucniton that confirms your string is a DNA string 
# dont know where the code we getting is from, could download wrong file, etc
def validateSeq(dna_seq): 
    '''capitalises input DNA sequence and verifies that string contains only DNA nucleotides'''
    #tmpseq=dna_seq.upper()   # tmpseq is dna seq that initially gets pu tin converted to makes all characters uppercase, because lowercase and uppercase not equal and cant be compared
    #^ extracted & applied to dna seq externally + permannetly 
# does .upper() work in place? no, extracted from this funx (works in place = permanently changes the object)
#  now we run capitalised str tmpseq through loop to confirm it matches defined dna nucleotides
    for nuc in dna_seq: #every character in tmpseq labeled 'nuc' and compared to defined Nucleotides
        if nuc not in Nucleotides:
            return False #breaks the loop
    return dna_seq 

def countNucFreq(seq):
    '''counts nucleotide frequencies for DNA nucleotides'''
    tmpFreqDict={'G':0, 'C':0, 'A':0, 'T':0}  # dictionary={key:value}, here {'str':int}
    # dicitonaries: collection of key-value pair data, here nuc-frequency data. key must be str or int
    for nuc in seq:
        tmpFreqDict[nuc]+=1 #for the nuc element occuring in the str, the dicitonary value of that nuc increases by 1 and new value is assigned to the key
        # access :value by inputing dict[key]
    return tmpFreqDict
    # return dict(collections.Counter(seq))
    #  ^ here alt method using a python Counter tool to directly create a dictionary for nuc-freq data; but you should properly understand how they work before using them.
    #our 4 line code is easy to understand so thats also good 

def transcribe(seq):
    '''DNA->RNA by .replace all Thymine with Uracil '''
    return seq.replace('T', 'U')
 # code for DNA -> RNA is to replace T with U 

DNA_Complement={'G':'C', 'C':'G', 'A':'T', 'T':'A'}
# dictionary of complement sequence nucleotides for dna
def rev_complement(seq):
    """outputs complementary nucleotides in 5'->3' order for each nucleotide of input DNA sequence"""
    return''.join([DNA_Complement[nuc]for nuc in seq])[::-1]
    # because of key-value pairing, this function calls the complement nuc 'value' when an origin seq nuc 'key' is input 
    # if DNA_Complement['A'] -> returns corresponding value :'C' -> make a list[] = complementary DNA sequence 
    # original DNA sequence remains untouched with no elements being changed 
    # dictionary is not a function! it just reads out definitions
    # ''.join -> use '' as character that joins list[] items being concatenated
    #[::-1] -> read backwards from the end


#alternate, more pythonic solution. faster.
mapping=str.maketrans('GCAT', 'CGTA') 
#creates simpler dictionary
def rev_Comp(seq):
    return ''.join(seq.translate(mapping))[::-1] #instead of for loop, uses python function to  performs change-out of nuc in seq based on maketrans dictionary
'''creates complemenetary DNA sequence in 5'->3' orientation'''

def GCcontent(seq):
    '''gives % GC content in nucleic sequence. GC content affects melting temp of a dihelix and indicates presence of genes.'''
    return round((seq.count('C')+seq.count('G'))/len(seq)*100)
 #this uses pythonmethod for counting nuc in sequence
 #because diviosn, using round() to get whole number output

 # we could get GC content output within countFreqDic funciton but cannot access its internal count dicitonary outside of teh original funciton 

#if only want to look at GC content in certain section/subset of long NA, cna specify a range 
def GCcontent_subset(seq, k=20):  # can override k window size when using funciton using (seq, k=#)
    '''GC content in certain subset of long NA sequence. Default frame size is k'''
    res = []#define a list
    for i in range(0, len(seq)-k+1, k): # examines from 0 to end of last possible full k (length of seq -k+1), with jumps of k. -k=last position for k to end, +1 because range is exclusive 
        subseq=seq[i:i+k]
        res.append(GCcontent(subseq))
        #so this function loops through the sequence in specific window sizes and calculates GC content in these windows
    return res

def translate(seq, init_pos=0):
    '''Translates a DNA sequence into an a.a. sequence. Default init_pos=0.'''
    # accepts a DNA sequence at initialisation position '0' by default
    # use this init position to generate readnig frames, use parameter to shift our reads
    return[DNA_Codons[seq[pos:pos+3]]for pos in range (init_pos, len(seq)-2, 3)]
    # DNA_Codons is a dict{}
    # [pos:pos+3] sets read frame of 3 nuc codon [inclusive, exclusive), and outputs corresponding aa 
    # range (initial position) to (end of seq-2) being the last possible full codon RF
    # ',3' indicates to jump frame by 3 nuc for each subsequent reading 

def codon_usage(seq, aa):
    '''Provides the frequency of all occurring codons for specified amino acid. Input as (dna, 'aa').'''
    tmpList=[]
    for i in range (0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]]==aa: # value only added to list if encodes desired aa
            tmpList.append(seq[i:i+3]) # appending the codon (characters present i:i+3) as str to our list 
    freqDict=dict(collections.Counter(tmpList)) # using a py frequency Counter to create codon:freq dictionary of all the items in tmpList[] (like we did for nuc couting in py method)
    totalWeight=sum(freqDict.values())
    for seq in freqDict:# where seq = codon [key]
        freqDict[seq]=round(freqDict[seq]/totalWeight, 2) # occurrence of this codon [key]/all 'desired aa codons' present
        # :value changes from [codon key] frequency count to [codon key]'s proportion of total desired aa ocurrence
    return freqDict

def gen_ReadingFrames(seq):
    # Open Reading Frame = DNA string that contains no stop codons; minimum 3 aa long. ORF reading double stranded helix has 6 ORF, 3 forward direction, 3 in reverse direction on complememtary strand.
    #ORF ie Open to continuous Reading of mRNA in 3bp Frames without STOP codon.
    '''Generates the 6 possible Open Reading Frames (3 forward, 3 complementary) for translating a DNA sequence using DNA-based codons. ORF= *Open* to continuous *Reading* of mRNA in 3bp *Frames* without STOP codon'''
    frames=[]
    frames.append(translate(seq, 0))
    frames.append(translate(seq, 1))
    frames.append(translate(seq, 2))
    frames.append(translate(rev_complement(seq), 0))
    frames.append(translate(rev_complement(seq), 1))
    frames.append(translate(rev_complement(seq), 2))
    return frames

def proteins_from_RF(aaSeq):
    '''Compute all possible polypeptide chains from currnet aa sequence and return as list.'''
    currentProt=[]
    proteins=[]
    for aa in aaSeq:
        if aa == '_': #if coma across a STOP codon
            #careful to use one ' or two " so it matches presnetation style in your list!
            if currentProt:#if there is a currentProt (not empty)
                for p in currentProt:# p= current polypeptide chain 
                    proteins.append(p) # terminate current polypeptide concatenation and append to 'proteins' list     
                currentProt=[]#current polypeptide chain empties, no content.
        else:
            if aa=='M': #if come across START codon
                currentProt.append("") # current polypeptide chain begins; reads as an empty str but a str nonetheless. str len = 0. before this, there were no items in the list, the list was null. now, an item has begun in the list, therefore there is something present, therefore starts appending aa to polypeptide chain the polypeptide chain
            for i in range (len(currentProt)): # append an empty str to the current polypeptide chain -> starts to the at every location in length of current polypeptide chain in RF 
                currentProt[i] += aa # append current aa to the ongoing polypeptide str, location indicated does NOT change, location would imply which list item, not which character. here we are appending characters to a str. a longer str is still only one 1 list item. i=0. to the latest location in the polyppetide chain 
    return proteins  
    # because i in range, if we have multiple M START codons, will append current aa to item 0, then item 1, then item 2, etc
    # ie the first , longest protein can contain internal protein sequences in it, we dont terminate the first polypeptide str just bc we come across another START codon


def allproteins_allRFs(seq, startReadPos=0, endReadPos=0, ordered=False): 
    # Generate all RF
    # extract all proteins
    # Return list sorted/unsorted
    '''Compute all possible proteins for all ORFs; 
    \n Protein Search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2
    \n API can be used to pull protein info'''
    if endReadPos > startReadPos:
        RFs=gen_ReadingFrames(seq[startReadPos:endReadPos]) # if we only want to examine a specific subsect of the seq, we cna specify start and end reading positions
    else:
        RFs=gen_ReadingFrames(seq) # else gen all 6 RFs
    # ^ step 1 : gen list of desired RFs[] from either specified section or of all 6

    res=[] # empty list for generating all the proteins we find
    for RF in RFs:
        # loops through all RFs one by one, applying proteins_from_RF function -> returns list of proteins in each RF
        prots=proteins_from_RF(RF) #list of proteins from single RF
        for p in prots:
            res.append(p) # append all terminated polypeptide chains from each RF to res[] list; cumulating all protein[] lists
    if ordered:
        # sort our list of proteins [res] using py function 'sorted'
        return sorted (res, key=len, reverse=True) # ([list to sort], key characteristic to sort by 'length', reverse bc we want longest to shortest rather than default of shortest to longest)
    return res # outputs our final cumulated list of all proteins from all RFs   

# now applying real biological functions via National Center for Biotechnology Information ncbi
# ncbi > all databases > nucleotides filter > homo sapiens insulin, transcript variant 1 mRNA
# find translation = the protein
# click FASTA file for **DNA sequence**
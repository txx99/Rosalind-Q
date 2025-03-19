#ROSALIND stronghold exercises

# get nuc freqs in str
import collections
dna=('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
NucFreq=collections.Counter(dna) #creates nuc-freq dict{}
print(NucFreq['A'], NucFreq['C'], NucFreq['G'], NucFreq['T'])#access :value via dict['str_key']



#transcribe dna->rna
#replace T->U
t=('GATGGAACTTGACTACGTAAATT')
trb=t.replace('T', 'U') #is a copy, not in-place  
print(trb)
#print(t) #og unchanged, .replace makes copy



# reverse complement dna strand
s=("AAAACCCGGT")
scdict={'G':'C','C':'G','A':'T','T':'A'}
sc=[] # if inside for, it resets with every i unless we add more instrux
for i in s: #can apply dict to whole seq, have to apply to each character individually 
    sc.append(scdict[i]) #is  list, want concat str
sc=(''.join(sc)[::-1]) # [::-1] bc want compl str 5'->3'
print(sc)



#wascally wabbits, fibonacci seq but change the jumps
seq=[1,1] #start with one pair, one month to mature
k=3 
for i in seq:
    n=(k*seq[-2]+seq[-1]) # everyone present will be alive next time + everyone from 2 months ago can birth*3new pairs this time
    if n<=40 and k<=5: #exit seq 
        seq.append(n)

print(seq[5-1]) #how many present @ 5 months -1 for 0-based positions




# select highest GC content strand
pile=open('GC.txt')
pil=pile.readlines()
strands={}
current_str=[]
names=['']
for line in pil:
    line=line.replace("\n", '')
    if line.startswith('>'):
        current_str=''.join(current_str)
        strands[(names[-1])]=current_str
        strands[line]=''
        names.append(line)
        current_str=[]
    else:
        current_str.append(line)
#after last line, still need to add curr_str as :value
current_str=''.join(current_str)
strands[(names[-1])]=current_str
#cant use indexing on dictionary, instead make list of [keys] and can index that list ->dict[list_keys]

highv=0
highk='strand' #these outsid ethe loop so they dont get reset
for k in strands:
    if k.startswith(">"):
        nucs=collections.Counter(strands[k])
        #print(nucs)
        GCc=(((nucs['G'])+(nucs['C']))/(len(strands[k]))*100)
        if GCc > highv:
            highk=k
            highv=GCc
print('highest GC content:', highk,highv)




#counting point mutations
#how many bases not the same
s='GAGCCTACTAACGGGAT'
t='CATCGTAATGACGGCCT'

def dH_calc(a, b):
    '''calculate Hamming distance (# of point mutaxn) bw 2 homologous strands.'''
    if len(a)>1000 or len(b)>1000:
        print('dna strands over 1kbp, cannot compute.')
    else:
        dH=0
        a=list(a)
        b=list(b)    
        for i in range(len(a)):
            if a[i] != b[i]:
                dH +=1
        print('point mutations:', dH)

dH_calc(s, t)



#Mendelian Inheritance
lst = ['2', '2', '2']
k, m, n = map(float, lst)
t = sum(map(float, lst))
# manually list the parent combos * Probability of Y pheno
# remember to substract the haplotype from the total when they're the same for the second haplotype choosed
couples = [
            k*(k-1),  # AA x AA
            k*m,  # AA x Aa
            k*n,  # AA x aa
            m*k,  # Aa x AA
            m*(m-1)*0.75,  # Aa x Aa
            m*n*0.5,  # Aa x aa
            n*k,  # aa x AA
            n*m*0.5,  # aa x Aa
            n*(n-1)*0  # aa x aa
]
# (t-1) indicate that the first haplotype was select
print(round(sum(couples)/t/(t-1), 5))
# remember that if same denominator,can put the numerators together 
# manually do it
# YY YY-1
# YY Yy
# YY yy
# Yy YY
# Yy Yy-1 *.75
# Yy yy *.5
# yy YY
# yy Yy *.5
# yy yy-1*0


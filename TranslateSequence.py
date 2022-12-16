class Sequence:
    def __init__(self):
        # inputFile = input("Enter DNA Sequence txt File: ")
        #file = open(inputFile, "r")
       # self.sequence = file.read()
        self.complementDict = {"A":"T", "C":"G", "T":"A", "G":"C"}
        self.codonDict = {
            "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "ATT":"I", 
            "ATC":"I", "ATA":"I", "ATG":"M", "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "TCT":"S", "TCC":"S", 
            "TCA":"S", "TCG":"S", "TCT":"S", "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P", "ACT":"T", "ACC":"T", "ACA":"T", 
            "ACG":"T", "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A", "TAT":"T", "TAC":"T", "TAA":"Stop",
            "TAG":"Stop", "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "AAT":"N", "AAC":"N", "AAA":"K",
            "AAG":"K", "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E", "TGT":"C", "TGC":"C", "TGA":"Stop",
            "TGG":"W", "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGT":"S", "AGC":"S", "AGA":"R",
            "AGG":"R", "GGT":"G", "GGC":"G", "GGA":"G", "GGG": "G"
        }
    
    def processSequence(self, sequence):
        self.sequence = sequence.upper()
        self.sequence = sequence.replace("\n", "")
        self.sequence =sequence.replace("\r", "")
        self.length = len(sequence)

    # iterate over characters in string and returns true if input ONLY contains 'A', 'T', 'C', and/or 'G' ; else false
    def validateSequence(self, sequence):
        self.processSequence(sequence)

        if sequence == "":
            return ""
        else:
            return set(sequence).issubset({"A", "T", "C", "G"})

    # reverse the DNA sequence and return it
    def reverseSequence(self, sequence):
        self.processSequence(sequence)

        if sequence == "":
            return ""
        else:
            assert self.validateSequence(sequence)
            return sequence[::-1]

    # return complement for DNA sequence; iterate through list and change 'A' to 'T', 'T' to 'A', etc. O(n)
    def complement(self, sequence):
        self.processSequence(sequence)

        if sequence == "":
            return ""
        else:
            assert self.validateSequence(sequence)

            complement = "".join(self.complementDict.get(base, base) for base in sequence)
            return complement
        
    # return reverse complement for DNA sequence; i.e. reverse sequence and change 'A' to 'T', 'T' to 'A', etc 
    def reverseComplement(self, sequence):
        self.processSequence(sequence)

        if sequence == "":
            return ""
        else:
            assert self.validateSequence(sequence)

            reverseComplement = "".join(self.complementDict.get(base, base) for base in self.reverseSequence(sequence))
            return reverseComplement

    # return amino acid sequence corresponding to DNA sequence, allows offset of 0, 1, or 2
    def aminoAcidSequence(self, sequence, offset):
        self.processSequence(sequence)

        if sequence == "":
            return ""
        else:
            assert self.validateSequence(sequence)
            assert self.length >= 3

            protein_seq = ''
            for n in range(offset, len(sequence), 3):
                if sequence[n:n+3] in self.codonDict:
                    protein_seq += self.codonDict[sequence[n:n+3]]
            return protein_seq



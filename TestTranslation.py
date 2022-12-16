import unittest
from TranslateSequence import Sequence 

class TestSequence(unittest.TestCase):
    def setUp(self):
        self.ts = Sequence()

    def testValidateSequence(self):
        self.assertTrue(self.ts.validateSequence('ATCGATCG'))
        self.assertFalse(self.ts.validateSequence('QATGCCA'))
        self.assertFalse(self.ts.validateSequence('ATCGTAK'))
        self.assertFalse(self.ts.validateSequence('ATCGATc'))
        self.assertFalse(self.ts.validateSequence('ATqGATT'))
        self.assertFalse(self.ts.validateSequence(''))


    def testReverseStringEmpty(self):
        self.assertEqual("", self.ts.reverseSequence(""))

    def testReverseStringSimple(self):
        self.assertEqual("A", self.ts.reverseSequence("A"))

    def testReverseStringLong(self):
        self.assertEqual("ATCGATCG", self.ts.reverseSequence("GCTAGCTA"))
        self.assertEqual("TTTAAAGCTC", self.ts.reverseSequence("CTCGAAATTT"))

    def testComplementEmpty(self):
        self.assertEqual("", self.ts.complement(""))

    def testComplementSimple(self):
        self.assertEqual("T", self.ts.complement("A"))
        self.assertEqual("G", self.ts.complement("C"))
        self.assertEqual("C", self.ts.complement("G"))
        self.assertEqual("A", self.ts.complement("T"))

    def testComplementLong(self):
        self.assertEqual("ATGCATGC", self.ts.complement("TACGTACG"))
        self.assertEqual("TGGTATCCG", self.ts.complement("ACCATAGGC"))

    def testReverseComplementEmpty(self):
        self.assertEqual("", self.ts.reverseComplement(""))

    def testReverseComplementSimple(self):
        self.assertEqual("A", self.ts.reverseComplement("T"))
        self.assertEqual("G", self.ts.reverseComplement("C"))
        self.assertEqual("C", self.ts.reverseComplement("G"))
        self.assertEqual("T", self.ts.reverseComplement("A"))

    def testReverseComplementLong(self):
        self.assertEqual("ATCGATCG", self.ts.reverseComplement("CGATCGAT"))
        self.assertEqual("TGTGCATAG", self.ts.reverseComplement("CTATGCACA"))

    def testAminoAcidSequenceEmpty(self):
        self.assertEqual("", self.ts.reverseComplement(""))

    def testAminoAcidSequenceShort0(self):
        self.assertEqual("K", self.ts.aminoAcidSequence("AAA", 0))
        self.assertEqual("V", self.ts.aminoAcidSequence("GTAT", 0))

    def testAminoAcidSequenceLong0(self):
        self.assertEqual("ASF", self.ts.aminoAcidSequence("GCCAGCTTT", 0))
        self.assertEqual("LDSKM", self.ts.aminoAcidSequence("CTGGACTCTAAAATG", 0))

    def testAminoAcidSequenceShort1(self):
        self.assertEqual("K", self.ts.aminoAcidSequence("GAAA", 1))
        self.assertEqual("L", self.ts.aminoAcidSequence("ATTGA", 1))

    def testAminoAcidSequenceLong1(self):
        self.assertEqual("PAL", self.ts.aminoAcidSequence('CCCCGCCCTT', 1))
        self.assertEqual("CATS", self.ts.aminoAcidSequence("TTGTGCTACTAGCA", 1))

    def testAminoAcidSequenceShort2(self):
        self.assertEqual("R", self.ts.aminoAcidSequence("GGAGA", 2))
        self.assertEqual("H", self.ts.aminoAcidSequence("TGCATT", 2))

    def testAminoAcidSequenceLong2(self):
        self.assertEqual("DEN", self.ts.aminoAcidSequence('GCGATGAGAAT', 2))
        self.assertEqual("WALK", self.ts.aminoAcidSequence("AATGGGCCTTGAAATA", 2))

if __name__ == '__main__':
    unittest.main()
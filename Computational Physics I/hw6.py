from hw6 import  SparseArray

sa = SparseArray (100) # All cells will have value None

sa[23] = 'C'

sa[24] = [1 ,2] # at this moment linked list should have only two nodes

print(sa[23])

sa[25] # should return None , but internally no node #25 should exist .
sa[100] = 1 # should raise IndexError
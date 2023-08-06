cdef class ParallelTreeBank:

    def __init__(self,
                 folder1: str,
                 folder2: str,
                 pattern: str = None):
        self.__from_tree_bank = TreeBank(folder1, pattern)
        self.__to_tree_bank = TreeBank(folder2, pattern)
        self.removeDifferentTrees()

    cpdef removeDifferentTrees(self):
        cdef int i, j
        i = 0
        j = 0
        while i < self.__from_tree_bank.size() and j < self.__to_tree_bank.size():
            if self.__from_tree_bank.get(i).getName() < self.__to_tree_bank.get(j).getName():
                self.__from_tree_bank.removeTree(i)
            elif self.__from_tree_bank.get(i).getName() > self.__to_tree_bank.get(j).getName():
                self.__to_tree_bank.removeTree(j)
            else:
                i = i + 1
                j = j + 1
        while i < self.__from_tree_bank.size():
            self.__from_tree_bank.removeTree(i)
        while j < self.__to_tree_bank.size():
            self.__to_tree_bank.removeTree(j)

    cpdef int size(self):
        return self.__from_tree_bank.size()

    cpdef ParseTree fromTree(self, int index):
        return self.__from_tree_bank.get(index)

    cpdef ParseTree toTree(self, int index):
        return self.__to_tree_bank.get(index)

    cpdef TreeBank getFromTreeBank(self):
        return self.__from_tree_bank

    cpdef TreeBank getToTreeBank(self):
        return self.__to_tree_bank

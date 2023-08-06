cdef class ConstituentSpan:

    def __init__(self, constituent: Symbol, start: int, end: int):
        self.__constituent = constituent
        self.__start = start
        self.__end = end

    cpdef int getStart(self):
        return self.__start

    cpdef int getEnd(self):
        return self.__end

    cpdef Symbol getConstituent(self):
        return self.__constituent
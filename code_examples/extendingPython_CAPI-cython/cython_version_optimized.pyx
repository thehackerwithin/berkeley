cimport numpy as cnp

# NOTE: declaring the input timestamps as a numpy array greatly increases the
# speed because it allows the data to be accessed directly from the c-buffer
# without calling using any of the python machinery
def find_potential_event_ptrs(cnp.ndarray[cnp.uint64_t, ndim=1] timestamps,
                              size_t coinc_win, size_t min_ev_size,\
                              size_t max_ev_size):
    '''Take sorted timestamps and return ptrs and lens to locations in the 
       timestamp list that correspond to potential gamma ray events that have
       the following properties:
         - They all occur within coinc_win samples of each other
         - There are at least min_ev_size readouts
         - There are no more than max_ev_size readouts'''
    ptrs = []
    lens = []
    # Add some declarations
    cdef size_t i = 0
    cdef size_t ary_len = len(timestamps)
    cdef size_t n
    while i < ary_len:
        n = 1
        while (i+n < ary_len) and \
              (timestamps[i+n] <= timestamps[i] + coinc_win):
            n += 1
        if n >= min_ev_size and n <= max_ev_size:
            ptrs.append(i)
            lens.append(n)
        i += n
    return ptrs, lens

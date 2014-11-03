def find_potential_event_ptrs(timestamps, coinc_win, min_ev_size, max_ev_size):
    '''Take sorted timestamps and return ptrs and lens to locations in the 
       timestamp list that correspond to potential gamma ray events that have
       the following properties:
         - They all occur within coinc_win samples of each other
         - There are at least min_ev_size readouts
         - There are no more than max_ev_size readouts'''
    ptrs = []
    lens = []
    i = 0
    ary_len = len(timestamps)
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

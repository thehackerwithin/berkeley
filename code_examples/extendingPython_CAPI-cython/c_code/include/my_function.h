#ifndef MYFUNCTIONS_H
#define MYFUNCTIONS_H

#include <stdint.h>

/* C implementation of the find_potential_event_ptrs function. Note that the
 * arg parsing and value buidling is all contained in the pywrapper */
int find_potential_event_ptrs(uint64_t* timestamps, int ary_len, int coinc_win,
		              int min_ev_size, int max_ev_size,
			      PyObject* ptr_list, PyObject* len_list);

#endif //MYFUNCTIONS_H

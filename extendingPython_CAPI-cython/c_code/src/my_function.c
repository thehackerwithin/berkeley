#include <Python.h>
#include <stdint.h>

#include "my_function.h"

int find_potential_event_ptrs(uint64_t* timestamps, int ary_len, int coinc_win,
		              int min_ev_size, int max_ev_size, 
			      PyObject* ptr_list, PyObject* len_list)
{
  size_t i = 0;
  size_t n;
  while( i < ary_len )
  {
    n = 1;
    while( (i+n < ary_len) && (timestamps[i+n] <= timestamps[i] + coinc_win) )
    {
      n = n + 1;
    }
    if( (n >= min_ev_size) && (n <= max_ev_size) )
    {
      PyList_Append(ptr_list, PyInt_FromSize_t(i));
      PyList_Append(len_list, PyInt_FromSize_t(n));
    }
    i = i + n;
  }
  return 0;
}

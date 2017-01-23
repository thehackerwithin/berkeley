// Python headers
#include <Python.h>
#include "numpy/arrayobject.h"
// C-headers
#include <stdint.h>

// Our headers
#include "my_function.h"

// Our wrapper function - handles the communication between python and C
PyObject* wrap_find_potential_event_ptrs( PyObject* self, PyObject* args )
{
  // Pointers for holding input from python (use PyArg_ParseTuple)
  PyArrayObject* dtarr;         // Pointer to array object
  uint64_t* timestamps;		// Pointer to timestamp data array
  int ary_len;			// length of timestamp array
  int coinc_win;		// size of coincidence window
  int min_ev_size;		// min event size
  int max_ev_size;		// max event size

  // Extract input using PyArg_ParseTuple. If parsing fails, raise exception
  // i.e. return NULL
  if( !PyArg_ParseTuple( args, "Oiii", &dtarr, &coinc_win, &min_ev_size,
			 &max_ev_size ) )
  { return NULL; }

  // Get access to data in numpy array
  timestamps = (uint64_t*) dtarr->data;
  ary_len = dtarr->dimensions[0];

  // Create lists for use in our function
  Py_ssize_t list_size = 0;
  PyObject* ptr_list = PyList_New(list_size);
  PyObject* len_list = PyList_New(list_size);

  // Call our C function
  int ret = find_potential_event_ptrs(timestamps, ary_len, coinc_win,
		                      min_ev_size, max_ev_size, ptr_list,
				      len_list);

  // Return our lists pythonically
  return Py_BuildValue( "OO", ptr_list, len_list );
}

// ---------------- Make our wrapped function visible to python ---------------
static PyMethodDef AnalysisMethods[] = 
{
  {"find_potential_event_ptrs", (PyCFunction)wrap_find_potential_event_ptrs,
   METH_VARARGS, "C-version of find_potential_event_ptrs"},
  {NULL, NULL}	// Ends the method list
};

// Initialize our module with the methods we've defined
PyMODINIT_FUNC initc_version(void)
{
  (void) Py_InitModule("c_version", AnalysisMethods );
  import_array();	// load numpy
};

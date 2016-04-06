#include <Python.h>
#include "numpy/arrayobject.h"
#include <math.h>

PyObject* sum_circle(PyObject* self, PyObject* args)
  {
    PyArrayObject *data;
    double x, y, r;
    int status;

    // Extract input using PyArg_ParseTuple.
    status = PyArg_ParseTuple(args, "Oddd", &data, &x, &y, &r);

    // if parsing failed, raise exception by returning NULL
    if (!status) return NULL;

    // ------------------------------------------------------------------
    // Get pointer to data buffer of numpy array
    // assume that data area is aligned and in native byte order.
    npy_intp nd;
    npy_intp* dims;
    double* dptr;
    nd = PyArray_NDIM(data);    // number of dimensions
    dims = PyArray_DIMS(data);  // npy_intp array of length nd showing
                                // length in each dim.
    dptr = (double *)PyArray_DATA(data); // pointer to data.

    // check that data is 2-d
    if (nd != 2)
      {
        /* should set an error here! */
        return NULL;
      }

    // check that array is C-contiguous so we don't have to worry about
    // strides.
    if (!(PyArray_FLAGS(data) &
          (NPY_ARRAY_C_CONTIGUOUS | NPY_ARRAY_ALIGNED)))
      {
        /* should set an error here! */
        return NULL;
      }

    // check that array contains doubles
    if (PyArray_TYPE(data) != NPY_CDOUBLE)
      {
        /* should set an error here! */
        return NULL;
      }

    //--------------------------------------------------------------------
    // body

    double r2, sum;
    size_t i, j, imin, imax, jmin, jmax;

    imin = (size_t)floor((x - r) + 0.5);
    imax = (size_t)floor((x + r) + 0.5);
    jmin = (size_t)floor((y - r) + 0.5);
    jmax = (size_t)floor((y + r) + 0.5);

    r2 = r * r;

    sum = 0.0;
    for (j=jmin; j<=jmax; j++)
      {
        for (i=imin; i<=imax; i++)
          {
            if ((i - x)*(i - x) + (j - y)*(j - y) < r2)
              sum += dptr[j*dims[1] + i];
          }
      }

    // ---------------------------------------------------------------------
    // put `sum` into a Python object for return
    return Py_BuildValue("d", sum);
  }


// ---------------- Make our wrapped function visible to python ---------------
static PyMethodDef GeometryMethods[] = {
  {"sum_circle", (PyCFunction)sum_circle, METH_VARARGS,
   "Sum array values within a circle."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef geometry_c =
{
    PyModuleDef_HEAD_INIT,
    "geometry_c", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    GeometryMethods
};

PyMODINIT_FUNC PyInit_geometry_c(void)
{
    return PyModule_Create(&geometry_c);
};

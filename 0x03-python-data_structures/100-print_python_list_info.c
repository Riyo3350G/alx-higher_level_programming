#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int idx;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);
	for (idx = 0; idx < size; idx++)
		printf("Element %i: %s\n", index, Py_TYPE(object->ob_item[idx])->tp_name);
}

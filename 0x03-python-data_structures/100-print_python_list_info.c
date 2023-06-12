#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, a;
	int allocate;
	PyObject *object;

	allocate = ((PyListObect *)p)->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (a = 0; a < size; a++)
	{
		printf("Element %d: ", a);

		object = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}

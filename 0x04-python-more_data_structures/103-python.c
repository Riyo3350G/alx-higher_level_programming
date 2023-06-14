#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_list - Prints basic information about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, allocated, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, print_size;
	PyBytesObject *bytes = (PyBytesObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(var->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", var->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (var->ob_size > 10)
		print_size = 10;
	else
		print_size = var->ob_size + 1;

	printf("  first %d bytes: ", print_size);
	for (i = 0; i < print_size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (print_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

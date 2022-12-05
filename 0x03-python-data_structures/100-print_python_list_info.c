#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: a python object
 * Return: void.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	ssize_t list_s = 0, i = 0;

	/* check */
	if (!p || !PyList_Check(p))
		return;
	/* cast to list */
	list = (PyListObject *) p;
	list_s = PyList_Size(p);
	/* printer */
	printf("[*] Size of the Python List = %ld\n", list_s);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list_s; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

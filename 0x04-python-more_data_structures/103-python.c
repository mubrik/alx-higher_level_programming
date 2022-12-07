#define PY_SSIZE_T_CLEAN
#include "Python.h"

/**
 * print_python_bytes - prints info about a python strin
 * @p: a python object
 * Return: void.
 */
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
	ssize_t by_s = 0;
	int i = 0, iter = 0;
	/* check */
	printf("[.] bytes object info\n");
	if (!p || !PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	by_s = PyByteArray_Size(p);
	PyBytes_AsStringAndSize(p, &str, &by_s);
	/* printer */
	printf("  size: %ld\n", by_s);
	printf("  trying string: %s\n", str);
	iter = by_s < 10 ? by_s : 10;
	printf("  first %d bytes: ", iter + 1);
	for (i = 0; i < iter; i++)
	{
		printf("%02x", str[i] & 0xff);
		if (i != iter - 1)
			printf(" ");
	}
	/* nuul byte */
	if (iter < 10)
		printf(" 00");
	printf("\n");
}

/**
 * print_python_list - prints info about a python list
 * @p: a python object
 * Return: void.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	ssize_t list_s = 0, i = 0;

	/* check */
	if (!p || !PyList_Check(p))
		return;
	printf("[*] Python list info\n");
	/* cast to list */
	list = (PyListObject *) p;
	list_s = PyList_Size(p);
	/* printer */
	printf("[*] Size of the Python List = %ld\n", list_s);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list_s; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

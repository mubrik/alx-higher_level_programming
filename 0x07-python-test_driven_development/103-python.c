#include "Python.h"
#include <stdio.h>

/**
 * is_type - checks Pyobject type
 * @p: a python object
 * @str: string of type to check
 * Return: 1 if true 0 else.
 */
int is_type(PyObject *p, char *str)
{
	if (!p)
		return (0);
	if (strcmp(p->ob_type->tp_name, str) == 0)
		return (1);
	return (0);
}

/**
 * print_python_float - prints info about a python float obj
 * @p: a python object
 * Return: void.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *fl;
	char *buf = NULL;
	/* check */
	fflush(stdout);
	printf("[.] float object info\n");
	if (!p || !is_type(p, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	fl = (PyFloatObject *) p;
	buf = PyOS_double_to_string(fl->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
	fflush(stdout);
}

/**
 * print_python_bytes - prints info about a python byte obj
 * @p: a python object
 * Return: void.
 */
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
	ssize_t by_s = 0;
	int i = 0, iter = 0;
	Py_buffer buf_view;
	/* check */
	fflush(stdout), printf("[.] bytes object info\n");
	if (!p || !is_type(p, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	/* set buf view to return chars */
	buf_view.format = "c";
	/* cast to a var object which hold size attribute */
	by_s = ((PyVarObject *) p)->ob_size;
	if (PyObject_GetBuffer(p, &buf_view, 0) == -1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	/* cast to char * */
	str = (char *) buf_view.buf;
	/* printer */
	printf("  size: %ld\n", by_s);
	printf("  trying string: %s\n", str);
	iter = by_s < 10 ? by_s : 10;
	printf("  first %d bytes: ", iter < 10 ? iter + 1 : iter);
	for (i = 0; i < iter; i++)
	{
		printf("%02x", str[i] & 0xff);
		if (i != iter - 1)
			printf(" ");
	}
	/* release malloc buffer */
	PyBuffer_Release(&buf_view);
	/* nuul byte */
	if (iter < 10)
		printf(" 00");
	printf("\n"), fflush(stdout);
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
	/* check null, check, type */
	fflush(stdout), printf("[*] Python list info\n");
	if (!p || !is_type(p, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	/* cast to list */
	list = (PyListObject *) p;
	/* cast to a var object which hold size attribute */
	list_s = ((PyVarObject *) p)->ob_size;
	/* printer */
	printf("[*] Size of the Python List = %ld\n", list_s);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list_s; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (is_type(item, "bytes"))
			print_python_bytes(item);
		else if (is_type(item, "float"))
			print_python_float(item);
	}
	fflush(stdout);
}

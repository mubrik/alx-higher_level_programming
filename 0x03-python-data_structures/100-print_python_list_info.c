#include <python3.4/Python.h>

/**
	* _strlen - returns the length of a string.
	* @src_ptr: str buffer
	* Return: int length
	*/
int _strlen(const char *src_ptr)
{
	/* implement null checking? orignal doesnt seem to? */
	/* checking if the current value of pointer not null */
	if (*src_ptr != 0)
	{
		/* move the pointer foward and call the function again adding 1! */
		src_ptr++;
		return (1 + _strlen(src_ptr));
	}

	return (0);
}

/**
	* _strcmp - function that compares two strings.
	* @s1_ptr: src 1 pointer char
	* @s2_ptr: src 2 pointer char
	* Return: 0 if equal -1 if s1 less than s2
	* +1 if greater
	*/
int _strcmp(const char *s1_ptr, const char *s2_ptr)
{
	int s1_len, s2_len, iter, max_iter, compare_res;

	/* get len of both */
	s1_len = _strlen(s1_ptr);
	s2_len = _strlen(s2_ptr);
	compare_res = 0;

	/* iterate using longer len*/
	max_iter = s1_len >= s2_len ? s1_len : s2_len;
	iter = 0;

	while (iter < max_iter)
	{
		/* compare val of pointers*/
		compare_res = s1_ptr[iter] - s2_ptr[iter];
		/* if not equal break */
		if (compare_res != 0)
			break;
		iter++;
	}

	return (compare_res);

}

/**
 * print_python_list_info - prints info about a python list
 * @p: a python object
 * Return: void.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	ssize_t list_s, list_a, i;

	/* check */
	if (!p)
		return;
	if (_strcmp(p->ob_type->tp_name, "list"))
		return;
	/* cast to list */
	list = (PyListObject *) p;
	list_s = Py_SIZE(list);
	list_a = list->allocated;
	printf("[*] Size of the Python List = %ld \n", list_s);
	printf("[*] Allocated = %ld \n", list_a);
	for (i = 0; i < list_s; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

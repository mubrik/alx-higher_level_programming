#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is alindrome
 * @head : head of list
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int list_s = 0, list_half = 0, i = 0, j = 0, c = 0, *num_list;

	if (!head)
		return (1);
	tmp = *head;
	/* get list size to create */
	while (tmp)
		tmp = tmp->next, list_s++;
	/* efficiency addition, check length */
	if (list_s == 1)
		return (1);
	list_half = list_s / 2;
	/* creat list, only half sizzed for space efficiency */
	num_list = malloc(sizeof(int) * list_half);
	if (!num_list)
		return (0);
	/* start */
	tmp = *head;
	/* fill up mallocd list from middway of linked list */
	for (i = 0; tmp; i++)
	{
		c = list_s % 2 != 0 ? list_half : list_half - 1;
		if (i > c)
			num_list[j] = tmp->n, j++;
		tmp = tmp->next;
	}
	/* start comparison from end of list and start of linked l */
	tmp = *head;
	for (i = list_half - 1; i >= 0; i--)
	{
		if (tmp->n != num_list[i])
			return (0);
		tmp = tmp->next;
	}
	return (1);
}

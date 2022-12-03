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
	int list_s = 0, i = 0, *num_list;

	if (!head)
		return (1);
	tmp = *head;
	/* get list size to create */
	while (tmp)
		tmp = tmp->next, list_s++;
	/* creat list */
	num_list = malloc(sizeof(int) * list_s);
	if (!num_list)
		return (0);
	/* start */
	tmp = *head;
	/* fill up list */
	for (; tmp; i++)
		num_list[i] = tmp->n, tmp = tmp->next;
	/* start comparison from end of list and start of linked l */
	tmp = *head;
	for (i = list_s - 1; tmp; i--)
	{
		if (tmp->n != num_list[i])
			return (0);
		tmp = tmp->next;
	}
	return (1);
}

#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *n_node, *p_node = NULL;

	if (!head)
		return (NULL);

	node = *head;

	while (node)
	{
		if (node->n > number)
		{
			/* create node */
			n_node = malloc(sizeof(listint_t));
			if (!n_node)
				return (NULL);
			n_node->n = number;
			/* replace prev nodes next */
			if (p_node)
				p_node->next = n_node;
			else /* first elem */
				*head = n_node;
			/* point new node next to current node */
			n_node->next = node;
			return (n_node);
		}
		/* iterate */
		p_node = node, node = node->next;
	}

	/* didnt find a node with greater number, add to end */
	return (add_nodeint_end(head, number));
}

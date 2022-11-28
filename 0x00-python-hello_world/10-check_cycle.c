#include "lists.h"

/**
 * _add_nodeaddr - adds a new node at the beginning of a listint_t.
 * @head: ptr to head ptr to list first elem
 * @addr: number
 * Return: ptr to new node.
 */
list_adrs_t *_add_nodeaddr(list_adrs_t **head, void *addr)
{
	list_adrs_t *n_node;

	/* alloc space */
	n_node = malloc(sizeof(list_adrs_t));
	if (!n_node)
		exit(98); /* replace with fail? */
	/* struct attribs */
	n_node->address = (uintptr_t) addr;
	/* swappp */
	n_node->next = *head, *head = n_node;
	return (n_node);
}

/**
 * _is_in_addlist - checks for an address in  a list_adrs_t.
 * @head: ptr to head ptr to list first elem
 * @addr: adress
 * Return: 1 if in, 0 else
 */
int _is_in_addlist(list_adrs_t *head, void *addr)
{
	list_adrs_t *node;

	node = head;
	if (!node)
		return (0);
	/* iterate */
	while (node)
	{
		if (node->address == ((uintptr_t) addr))
			return (1);
		node = node->next;
	}
	return (0);
}

/**
 * _free_listaddr - function that frees a listint_t list.
 * @head: head ptr to list first elem
 * Return: void
 */
void _free_listaddr(list_adrs_t *head)
{
	list_adrs_t *tmp, *node;
	/* simple check */
	if (!head)
		return;
	/* else iterate and free */
	node = head;
	while (node)
	{
		/* cp the next ptr/null to tmp, free the current ptr memory */
		tmp = node->next, free(node), node = tmp; /* cp the tmp ptr to node */
	}
}

/**
 * check_cycle - checks for loop cycle
 * @list: head ptr to list first elem
 * Return: size of freed elem.
 */
int check_cycle(listint_t *list)
{
	listint_t *node, *tmp;
	list_adrs_t *addr_h = NULL;

	if (!list)
		return (0);
	/* cp head */
	node = list;
	/* iterate */
	while (node)
	{
		tmp = node->next;
		if (!_is_in_addlist(addr_h, (void *)node))
			_add_nodeaddr(&addr_h, (void *)node);
		else
		{
			_free_listaddr(addr_h);
			return (1);
		}
		node = tmp;
	}

	/* free our addr list */
	_free_listaddr(addr_h);
	return (0);
}

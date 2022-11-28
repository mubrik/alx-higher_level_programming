#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdint.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct list_adrs - singly linked list
 * @address: unsigned integer
 * @next: points to the next node
 * Description: keeps track of addresses
 */
typedef struct list_adrs
{
	uintptr_t address;
	struct list_adrs *next;
} list_adrs_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
void _free_listaddr(list_adrs_t *head);
int _is_in_addlist(list_adrs_t *head, void *addr);
list_adrs_t *_add_nodeaddr(list_adrs_t **head, void *addr);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

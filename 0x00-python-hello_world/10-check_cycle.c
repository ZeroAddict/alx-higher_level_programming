#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!list || !list->next)
		return (0);

	tortoise = list;
	hare = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;       /* Move tortoise one step */
		hare = hare->next->next;        /* Move hare two steps */

		if (tortoise == hare)           /* If they meet, there's a cycle */
			return (1);
	}

	return (0); /* No cycle found */
}

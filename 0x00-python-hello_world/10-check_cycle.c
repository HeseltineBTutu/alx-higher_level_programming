#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
	{
		return (0);
	}
	listint_t *tortoise = list;
	listint_t  *hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}

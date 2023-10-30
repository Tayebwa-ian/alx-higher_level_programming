#include "lists.h"
/**
 *check_cycle - check if there is a cycle in a list
 *list: the list to check
 *Return: 1 on success and 0 on failure
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (list == NULL)
	{
		free_listint(list);
		return (0);
	}
	while (current != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}

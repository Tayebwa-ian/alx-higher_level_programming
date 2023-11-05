#include "lists.h"

/**
 * list_len -  function that returns the number of elements in a linked list_t
 *@h: the linked list
 *Return: number of elements in a list
 */
size_t list_len(listint_t *h)
{
	int i = 1;

	if (h == NULL)
		return (0);

	while (h->next != NULL)
	{
		h = h->next;
		i++;
	}
	return (i);
}

/**
 *reverse_list - reverse a linked list
 *@head: head of the list
 *Return: address of reversed list or NULL
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *temp = NULL, *nxt;

	if (head == NULL)
		return (NULL);
	while (head != NULL)
	{
		nxt = head->next;
		head->next = temp;
		temp = head;
		head = nxt;
	}
	return (temp);
}
/**
 *is_palindrome - check if a list is a palindrome
 *@head: head of the list
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *current;
	size_t len;

	if (head== NULL)
		return (0);
	else if (*head == NULL)
		return (1);
	current = *head;
	len = list_len(current);
	if (len % 2 != 0)
		return (0);
	rev = reverse_list(current);
	while (current != NULL && rev != NULL)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	}
	return (1);
}

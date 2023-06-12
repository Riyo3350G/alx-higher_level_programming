#include "lists.h"

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1;
	listint_t *temp1, *temp2;

	if (*head == NULL || (*head)->next == NULL)
                return 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
	}

	prev->next = NULL;

	second_half = reverse_list(second_half);

	temp1 = *head;
	temp2 = second_half;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			palindrome = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	second_half = reverse_list(second_half);

	if (fast != NULL)
	{
		prev->next = slow;
		slow->next = second_half;
	}
	else
	{
		prev->next = second_half;
	}

	return palindrome;
}


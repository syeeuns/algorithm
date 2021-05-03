#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *next;
};

void printLinkedList(struct node *p){
    while (p != NULL){
        printf("%d\n", p->value);
        p = p->next;
    }
}

int main()
{
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;

    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));

    one->value = 1;
    two->value = 2;
    three->value = 3;

    head = one;
    one->next = two;
    two->next = three;
    three->next = NULL;

    printLinkedList(head);
}

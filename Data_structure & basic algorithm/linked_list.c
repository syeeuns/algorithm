#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *next;
};

void insertBeginning(struct node** head, int v){
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->value = v;
    newNode->next = (*head);
    (*head) = newNode;
};

void insertEnd(struct node** head, int v){
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    struct node* last = (*head);
    newNode->value = v;
    newNode->next = NULL;

    if ((*head) == NULL){
        (*head) = newNode;
        return;
    }

    while (last->next != NULL){
        last = last->next;
    }

    last->next = newNode;
    return;
};

void insertAfter(struct node* node, int v){
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->value = v;

    if (node == NULL){
        printf("the given node NULL");
        return;
    }

    newNode->next = node->next;
    node->next = newNode;
};

void deleteNode(struct node** head, int v){
    struct node* temp = *head;
    struct node* prev;

    // case 1. beginnig
    if (temp != NULL && temp->value == v){
        (*head) = temp->next;
        free(temp);
        return;
    }

    // case 2. Middle
    while (temp != NULL && temp->value != v){
        prev = temp;
        temp = temp->next;
    }

    // not found key
    if (temp == NULL){
        printf("not found..");
        return;
    }
    // found key
    prev->next = temp->next;
    free(temp);
}


void printLinkedList(struct node *p){
    while (p != NULL){
        printf("%d ----> ", p->value);
        p = p->next;
    }
}

int main()
{
    struct node *head = NULL;

    insertBeginning(&head, 1);
    insertEnd(&head, 2);
    insertEnd(&head, 3);
    insertAfter(head->next, 4);
    insertBeginning(&head, 5);


    printLinkedList(head);
    printf("\n start delete..\n\n");
    deleteNode(&head, 2);
    printLinkedList(head);
}
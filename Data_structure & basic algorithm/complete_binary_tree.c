#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    int key;
    struct Node *left, *right;
};

struct Node *newNode (char k){
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->key = k;
    node->left = NULL;
    node->right = NULL;
    return node;
};

int countNumNodes (struct Node *root){
    if (root == NULL)
        return 0;
    else{
        return (countNumNodes(root->left) + countNumNodes(root->right) + 1);
    }
};

bool checkComplete(struct Node *root, int index, int numberNodes){
    if (root == NULL)
        return true;
    if (index >= numberNodes)
        return false;

    return (checkComplete(root->left, 2 * index + 1, numberNodes) && checkComplete(root->left, 2 * index + 2, numberNodes))
};

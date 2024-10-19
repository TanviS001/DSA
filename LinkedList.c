#include <stdio.h>
#include <stdlib.h>

int main() {
    struct node{
        int data;
        struct node *next;
    };
    
    struct node *new1;
    new1 = (struct node *)malloc(sizeof(struct node));
    new1->data = 10;
    new1->next = NULL;
    
    struct node *new2;
    new2 = (struct node *)(malloc(sizeof(struct node)));
    new2->data = 20;
    new2->next = NULL;
    
    new1->next = new2;

    printf("Node 1 data: %d\n", new1->data);
    printf("Node 2 data: %d\n", new2->data);

    return 0;
}

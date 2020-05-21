#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

typedef struct Node Node;
typedef struct Singly_LList Singly_LList;

struct Node {
    int val;
    Node *next;
    Node *prev;
};

struct Singly_LList {
    Node *first;
    int size;
};

/*
* list constructor
*/
Singly_LList *New_List() {
    Singly_LList *l = (Singly_LList *)malloc(sizeof(Singly_LList));
    l->first = NULL;
    l->size = 0;
    return l;
}

/*
* node constructor
*/
Node *New_Node(int val) {
    Node *n = (Node *)malloc(sizeof(Node));
    n->next = NULL;
    n->prev = NULL;
    n->val = val;
    return n;
}

/*
* insert element to the list
*/
void insert(Singly_LList *l, int val) {
    Node *n = New_Node(val);

    if(l->first) {
        Node *first = l->first;
        n->prev = first->prev;
        n->next = first;
        first->prev->next = n;
        first->prev = n;
        l->first = n;
    }
    else {
        n->next = n;
        n->prev = n;
        l->first = n;
    }
    l->size++;
}

/*
* return element with a given key 
*/
Node *search(Singly_LList *l, int val) {
    Node *node = l->first;

    for(int i = 0 ; i < l->size ; i++) {
        if(node->val == val) {
            //printf("Element with key %d found!", val);
            return node;
        }
        node = node->next;
    }
    //printf("Cant't find element with key %d!", val);
    return NULL;
}

/*
* delete first occurrence of element from list 
*/
void delete(Singly_LList *l, int val) {
    Node *node = l->first;

    
    if(node && node->val == val) {
        if(l->size == 1) {
            l->first = NULL;
        }
        else {
            l->first = node->next;

            node->prev->next = node->next;
            node->next->prev = node->prev;
        }
        free(node);
        l->size--;
    }
    else if (l->size > 1) {
        for(int i = 0 ; i < l->size ; i++) {
            if(node->val == val) {
                node->prev->next = node->next;
                node->next->prev = node->prev;
                l->size--;
                free(node);
                break;
            }
            node = node->next;
        }
        
    }
}

/*
* print all elements in the list
*/
void printList(Singly_LList l) {
    Node *node = l.first;
    printf("\n");
    for(int i = 0 ; i < l.size ; i++) {
        printf("%d\n", node->val);
        node = node->next;
    }
}

/*
* check if list is empty
*/
bool empty(Singly_LList *li) {
    return li->first == NULL;
}

/*
* return size of a list
*/
int size(Singly_LList *l) {
    return l->size;
}

/*
* merge two lists
*/
Singly_LList *merge(Singly_LList *l1, Singly_LList *l2) {
    if(l1->size == 0)
        return l2;
    if(l2->size == 0)
        return l1;
    else {
        Node *l1_f = l1->first;
        Node *l1_l = l1->first->prev;
        Node *l2_f = l2->first;
        Node *l2_l = l2->first->prev;
    
        l1_l->next = l2_f;
        l2_l->next = l1_f;

        l2_f->prev = l1_l;
        l1_f->prev = l2_l;

        l1->size += l2->size;
        return l1;
    }
}

int main() {
    Singly_LList *l1 = New_List();

    insert(l1, 6);
    insert(l1, 5);
    insert(l1, 4);
    insert(l1, 3);
    insert(l1, 2);
    insert(l1, 1);

    Singly_LList *l2 = New_List();

    insert(l2, 12);
    insert(l2, 11);
    insert(l2, 10);
    insert(l2, 9);
    insert(l2, 8);
    insert(l2, 7);

    printList(*l1);
    Singly_LList *l3 = merge(l1, l2);
    printList(*l3);

    delete(l3,1);
    delete(l3,6);
    delete(l3,12);
    delete(l3,11);

    printList(*l3);

    Singly_LList *l4 = New_List();
    int elements[1000];
    srand(time(NULL));
    for(int i=0; i<1000; i++) {
        int x = rand()%1000;
        insert(l4, x);
        elements[i] = x;
    }

    printf("List size: %d\n", size(l4));

    clock_t start, end;
    double cpu_time_used = 0;
    for(int i=0; i<1000; i++) {
        
        start = clock();
        if(!search(l4, elements[i])) {
            printf("nie znaleziono %d\n", elements[i]);
        }
        end = clock();
        cpu_time_used += (double)(end - start);
    }
    printf("Average time: %f\n", cpu_time_used/CLOCKS_PER_SEC/1000);

    return 0;
}
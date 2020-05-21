#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

#define INIT_SIZE 5

double fifo[ INIT_SIZE ];
int head = 0;
int tail = 0;


/*
* wrzuc element do kolejki na koniec
*/
bool enqueue(double element) {
    if((tail + 1) % INIT_SIZE == head) {
        return false;
    }

    fifo[tail] = element;
    tail = (tail + 1) % INIT_SIZE;
    return true;
}


/*
* sciagnij element z kolejki z poczatku
*/
double *dequeue() {
    if(tail == head) {
        return NULL;
    }

    int temp = head;
    head = (head + 1) % INIT_SIZE;
    return &fifo[temp];
}


/*
* sprawdz czy kolejka pusta
*/
bool empty() {
    return tail == head;
}


//wypisz liczbe elementów
int size() {
    return head <= tail ? tail-head : INIT_SIZE - head + tail;
}

int main() {
    enqueue(2);
    enqueue(3);
    enqueue(4);
    printf("%f\n", *dequeue());
    printf("%f\n", *dequeue());
    printf("%f\n", *dequeue());
    enqueue(5);
    enqueue(6);
    enqueue(7);
    enqueue(8);
    printf("empty: %s\n", empty() ? "true" : "false");
    printf("size: %d\n", size());
    printf("%f\n", *dequeue());
    printf("%f\n", *dequeue());
    printf("%f\n", *dequeue());
    printf("%f\n", *dequeue());
    printf("empty: %s\n", empty() ? "true" : "false");
    printf("size: %d\n", size());

    return 0;
}
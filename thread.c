#include <pthread.h>
#include <stdio.h>

typedef struct threadData{
    int threadId;
    char name[20];
}ThreadData;
typedef char caracter;

void * holaMundo(void *arg){
    ThreadData *myData = (ThreadData *)arg;
    printf("hola desde el hilo y mi id es %d\n",myData -> threadId);
    pthread_exit(NULL);
}

int main(){
    for (int i = 0; i < 100; i++){
        ThreadData myData;
        pthread_t threadId;
        myData.thread =i;
        pthread_create(&threadId,NULL,holaMundo,NULL);
    }
    pthread_exit(NULL);
    printf("nunca llega");
}
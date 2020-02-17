#include <stdio.h>

int main(void)
{
    char name[12];
    printf("What's your name? ");
    scanf("%s", name);
    printf("Hello %s!\n", name);
    if (name == "chocolat")
    {
        printf("Non CHOCOLATINE\n");
    }
    else if (name != "bien")
    {
        printf("Bien\n");
    }
    
}
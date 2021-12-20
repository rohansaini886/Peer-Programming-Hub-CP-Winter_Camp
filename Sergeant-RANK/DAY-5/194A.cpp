#include <cstdio>

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    printf("%d\n", k <= n * 3 ? n * 3 - k : 0);
    return 0;
}

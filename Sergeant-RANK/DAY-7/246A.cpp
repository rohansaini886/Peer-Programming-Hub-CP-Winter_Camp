#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    if (n > 2)
    {
        for (int i = 2; i <= n; ++i)
        {
            cout << i << " ";
        }
        cout << 1 << endl;
    }
    else
    {
        cout << -1 << endl;
    }
    return 0;
}

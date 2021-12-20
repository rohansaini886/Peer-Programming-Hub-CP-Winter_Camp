#include <iostream>

using namespace std;

int main()
{
    int n, x, y;
    cin >> n >> x >> y;
    int clones = (n * y + 99) / 100 - x;
    if (clones < 0)
    {
        clones = 0;
    }
    cout << clones << endl;
    return 0;
}

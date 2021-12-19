#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int result(0), count(1);
    for (size_t i = 1; i < s.length(); ++i)
    {
        if (s[i] == s[i-1])
        {
            count += 1;
        }
        else
        {
            result += (count + 4) / 5;
            count = 1;
        }
    }
    result += (count + 4) / 5;
    cout << result << endl;
    return 0;
}

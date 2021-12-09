#include<bits/stdc++.h>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while(t--) {
        string n;
        cin >> n;
        if((n.back() - '0') % 2 == 0) {
            cout << "0\n";
            continue;
        }
        if((n[0] - '0') % 2 == 0) {
            cout << "1\n";
            continue;
        }
        int count_2 = count(n.begin(), n.end(), '2');
        int count_4 = count(n.begin(), n.end(), '4');
        int count_6 = count(n.begin(), n.end(), '6');
        int count_8 = count(n.begin(), n.end(), '8');
        if(count_2 > 0 || count_4 > 0 || count_6 > 0 || count_8 > 0) {
            cout << "2\n";
            continue;
        }
        cout << "-1\n";
    }
    return 0;
}

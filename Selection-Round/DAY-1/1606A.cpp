#include <bits/stdc++.h>
using namespace std;
#define sz(c)               (int)(c).size()
int main(){
    int t;
    cin >> t;
    while(t--){
        string s;
    	cin >> s;
    
    	if (s[0] != s[sz(s) - 1])
    		s[0] = s[sz(s) - 1];
    
    	cout << s << endl;
    }
    return 0;
}

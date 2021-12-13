#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll b,k;
    cin>>b>>k;
    ll res=0;
    while(k--)
    {
        ll ele;
        cin>>ele;
        if(k==0)
        {
            res+=ele;
           // cout<<"elel"<<ele<<endl;
        }
        else res+=(b*ele);


    }
    //cout<<res<<endl;
    if(res%2)
        cout<<"odd";
    else cout<<"even";

}

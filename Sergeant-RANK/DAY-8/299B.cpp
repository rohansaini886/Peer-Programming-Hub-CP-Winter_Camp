#include<bits/stdc++.h>

typedef long long int ll;
#define pp pair<ll,ll>
#define dbg printf("xxxx");
#define pi 3.1416

#define inf 1000000000000
#define max2(a,b) ((a<b)?b:a)
#define max3(a,b,c) max2(max2(a,b),c)
#define min2(a,b) ((a>b)?b:a)
#define min3(a,b,c) min2(min2(a,b),c)

using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);
    ll i,j,k;
    ll n,count=0;
    string s;

    cin>>n>>k;
    cin>>s;

    for(i=0;i<n;i++)
    {
        if(s[i]=='#')
        {
            count++;
        }

        else
            count=0;

        if(count>=k)
        {
            cout<<"NO";
            return 0;
        }
    }

    cout<<"YES";

    return 0;
}

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        int n;
        cin>>n;
        int arr[n];
        for(int k=0; k<n; k++){
            cin>>arr[k];
        }

        /*
        if(n==1 or n==2){
            cout<<"YES"<<endl;
            continue;
        }
        */


        vector<pair<int,int>> vall;
        int temp = 0;
        for(int k=0; k<n; k++){
            if(arr[k]==arr[k+1]){
                continue;
            }
            else{

                pair<int,int> p;
                p.first = temp;
                p.second = k;
                temp = k+1;

                vall.push_back(p);

            }
        }

        int co = 0;
        int flag = 0;

        for(int i=0; i<vall.size(); i++){
            //cout<<vall[i].first<<" " << vall[i].second<<endl;
            int l = vall[i].first;
            int r = vall[i].second;

            int isval = 0;
            if(l==0 || arr[l-1]>arr[l]){
                isval++;
            }
            if(r==n-1 || arr[r]<arr[r+1]){
                isval++;
            }
            if(isval==2){
                co++;
            }
           


        }
        if(co==1){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }





    }

    return 0;
}

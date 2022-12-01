#include<bits/stdc++.h>
using namespace std ;

int main (){
    int t ;
    cin>>t ;
    while(t--){
        int n ;
        int arr[n];
        for (int i=0 ; i<n ; i++) cin>>arr[i];
        if (n==1 || n==2){
            cout<<"YES"<<endl;
            continue;
        }
        else{
            vector<pair<int , int>> vt ;
            int co =0 ;
            int f , l ; 
            for (int i=0 ; i<n-1 ; i++){
                if (arr[i] == arr[i+1]){
                    co++;

                }
                else {
                  vt.push_back(make_pair(i, i+co));
                }

            }

            for (int i =0 ; i<vt.size()-1 ; i++){
                cout<<vt[i].first<< " "<<vt[i].second<<endl;
            }
        }
        
    }
}
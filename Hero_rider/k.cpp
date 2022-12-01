#include<bits/stdc++.h>
using namespace std ;

int main (){
    int t ;
    cin>>t ;
    while(t--){
        int n ;
        cin>>n ;
        int arr[n];
        for (int i=0 ; i<n ; i++) cin>>arr[i];
        if (n==1 || n==2){
            cout<<"YES"<<endl;
            continue;
        }
        else{
            vector<pair<int , int>> vt ;
           
            int temp = 0 ; 
            int l = 0 ;
            for ( int i=0 ; i<n ; i++){
                if (arr[i]== arr[i+1]){
                    continue;
                }
                else {
                    vt.push_back(make_pair(temp, i));
                    temp = i ;

                }

            }

            for (int i =0 ; i<vt.size()-1 ; i++){
                cout<<vt[i].first<< " "<<vt[i].second<<endl;
            }
        }
        
    }
}
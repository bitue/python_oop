#include<bits/stdc++.h>
using namespace std ;

int main(){
    int t;
    cin>>t ;
    while(t--){
        int n ; 
        cin>>n ;
        string s ;
        cin>>s ;
        int max_val =0 ;
        for (int i=0 ; i<s.length(); i++){
            
            int x = ( int(s[i]) - int('a')) +1;
            if (max_val < x ){
                max_val = x ;
            }


        }
        cout<<max_val<<endl;
    }
}
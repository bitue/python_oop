#include<bits/stdc++.h>
using namespace std ;

int main (){
    int sum_x =0 ;
    int sum_y =0 ;
    int sum_z =0 ;
    int n ;
    cin>> n ;
    for (int i =0 ; i<n ; i++){
        int x , y , z ;
        cin>>x>>y>>z ;
        
        sum_x+=x ;
        sum_y+=y ;
        sum_z+=z ;

    }

    // cout<<sum_x<<" "<<sum_y<<" "<<sum_z<<endl;

    if (sum_x ==0 && sum_y ==0 && sum_z ==0){
        cout<<"YES"<<endl;
    }
    else {
        cout<<"NO"<<endl;
    }

}
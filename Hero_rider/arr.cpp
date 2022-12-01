#include<bits/stdc++.h>
using namespace std ;

int main (){
    int t ;
    cin>>t ;
    while(t--){
        int n ;
        cin>>n ;
        int arr[n];
        int arr_sort[n];
        for (int i =0 ; i<n ; i++) {
            int x ;
            cin>>x ;
            arr[i] =x ;
            arr_sort[i]=x ;
            

        }

        

        sort(arr_sort, arr_sort+n);

        for(int i=0 ; i<n ; i++){
            if (arr[i] - arr_sort[n-1] != 0){
                cout<<arr[i]- arr_sort[n-1] <<" " ;
            }
            else {
                cout<<arr[i]-arr_sort[n-2]<<" ";
            }
        }

        
    }
}
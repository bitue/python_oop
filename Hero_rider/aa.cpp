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
        vector<int> vt ;
        vt.push_back(arr[0]);

        for (int i=0 ; i<n-1 ; i++){
            if (arr[i] != arr[i+1]){
                vt.push_back(arr[i+1]);
            }

        }

        // for (int i=0 ; i<vt.size(); i++){
        //     cout<<vt[i]<<" ";
        // }
        int co =0 ;
        bool flag = false ;

        for (int i=0 ; i<vt.size(); i++){
            if ( (i==0 || vt[i-1] > vt[i] ) && (i == vt.size()-1 || vt[i+1] > vt[i])) {
                co++ ;
            }
            if ( co >1 ) {
                cout<<"NO"<<endl;
                flag = true ;
                break ;
            }
        }
        if (flag == false &&  co ==1 ) {
            cout<<"YES"<<endl;
            break;
        }

    }
   

   
    
}
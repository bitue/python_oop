#include<bits/stdc++.h>
using namespace std ;

void cout_val (vector<pair<int, int>>  vt , int * arr , int n  ){
    int co =0 ;
    if (vt.size() == 1 ){
        cout<<"YES"<<endl;
        return ;
    }
    for (int i=0 ; i<vt.size(); i++){
        int x = vt[i].first ;
        int y = vt[i].second ;
        int max_val = vt[vt.size()-1].second ;

        if ( (x ==0 || arr[x-1] > arr[x] ) && ( y == max_val -1 || arr [y+1 == vt.size() ? vt.size() -1 : y+1] > arr[y] ) ) {
           co ++ ; 
        }

        if (co >1 ){
            cout<<"NO"<<endl;
            return  ;
        }

    }
    if (co ==1){
        cout<<"YES"<<endl;
        return  ;
    }


}

int main (){
    int t ;
    cin>>t ;
    while(t--){
        int n ;
        cin>>n ;
        int arr[n];
        for (int i=0 ; i<n ; i++) cin>>arr[i];
        vector<pair<int , int>> vt ;
        int temp =0 ;
        int co =0 ;
        

        for (int i=0 ; i<n ; i++){
            if (arr[i]==arr[i+1]) {
                co++;
            }
            else {
                vt.push_back(make_pair(temp, temp+co));
                co =0 ;
                temp = i+1 ;
            }

        }
        // for (int i =0 ; i<vt.size(); i++){
        //     cout<<"("<<vt[i].first<<", "<<vt[i].second<<")"<<endl;
        // }

        cout_val(vt, arr, n);

       
    }
}
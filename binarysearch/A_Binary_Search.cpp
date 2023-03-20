#include <iostream>
using namespace std;

int binarySearch(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    // target not found in array
    return -1;
}


int main(){
    int n, k;
    cin>>n>>k;
    vector<int> a(n);
    for (int i; i<n; i++){
        cin>>a[i];
    }
    
    for (int i; i<k; i++){
        int x;
        cin>>x;

        int l = 0;
        int h = n-1;
        bool flag = false;

        while (l<=h){
            int m = l-(h-l)/2;
            if (a[m]==x){
                flag = true;
                return;
            }else if(a[m]>x){
                h = m-1;
            }
            else{
                l = m+1;
            }
        }
        if(flag){
            cout<<"YES";
        }
        else{
            cout<<"NO";
        }
    }

}
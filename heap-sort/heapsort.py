#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        left = (2*i)+1
        right = (2*i)+2
        
        if left<n and right<n and arr[left]>arr[right]:
            arr[right],arr[left] = arr[left],arr[right]
        
        if left<n and arr[i] > arr[left]:
            arr[left], arr[i] = arr[i], arr[left]
            if left<n and right<n and arr[left]>arr[right]:
                arr[right],arr[left] = arr[left],arr[right]
            self.heapify(arr, n, left)
    
    # #Function to build a Heap from array.
    # def buildHeap(self,arr,n):
    #     # code here
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        for i in range(len(arr)):
            self.heapify(arr, n, i)
        

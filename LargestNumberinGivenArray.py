Program to find largest element in an array
Difficulty Level : Basic
 Last Updated : 22 Feb, 2021
Given an array, find the largest element in it. 
Example: 
 

Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100

Python:

# Python3 program to find maximum
# in arr[] of size n 

# python function to find maximum
# in arr[] of size n
def largest(arr,n):

	# return max using max 
	# inbuilt max() function
	return (max(arr))

# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)

#calculating length of an array

Ans = largest(arr,n)

#display max
print ("Largest in given array is",Ans)

# This code is contributed by Jai Parkash Bhardwaj


Java:

// Java Program to find maximum in arr[] 
class Test
{
	static int arr[] = {10, 324, 45, 90, 9808};
	
	// Method to find maximum in arr[]
	static int largest()
	{
		int i;
		
		// Initialize maximum element
		int max = arr[0];
	
		// Traverse array elements from second and
		// compare every element with current max 
		for (i = 1; i < arr.length; i++)
			if (arr[i] > max)
				max = arr[i];
	
		return max;
	}
	
	// Driver method
	public static void main(String[] args) 
	{
		System.out.println("Largest in given array is " + largest());
		}
}


ReferenceLink:  https://www.geeksforgeeks.org/c-program-find-largest-element-array/ 
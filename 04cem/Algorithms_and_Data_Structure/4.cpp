﻿#include <iostream>


using namespace std;

long long inv = 0;

int *merge(int *ar, int *tmp, int left_border, int right_border) {

	//full merging
	if (left_border == right_border) {
		tmp[left_border] = ar[left_border]; 
		return tmp;
	}
	int center = (left_border + right_border) / 2;//int not float
	int j = center + 1;
	int i = left_border;
	int count_for_invert = 0;

	//cutting
	int *left_cut = merge(ar, tmp, i, center);
	int *right_cut = merge(ar, tmp, j, right_border);
	int *sorted = left_cut == ar ? tmp : ar;
	
	
	for (int k = left_border; k <= right_border; k++) {
		if (i <= center && j <= right_border) {
			
			// cutting while elements excist in both arrs 
			if (left_cut[i] < right_cut[j]) {
				sorted[k] = left_cut[i++];
				count_for_invert++;
			}
			else
			{
				inv += center - left_border - count_for_invert +1;
				sorted[k] = right_cut[j++];

			}
		}
		//when no elements in rightct
		else if (i <= center) {
			sorted[k] = left_cut[i++];
		}
		else//when no elements in left
		{



			sorted[k] = right_cut[j++];
		}
	}
	return sorted;

}


int main(void)
{
	int n = 0;
	cin >> n;
	int *nums = new int[n];
	int *tmp = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> nums[i];

	}
	merge(nums, tmp, 0, n - 1);


	cout << inv;
	return 0;
}
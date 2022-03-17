public double findMedianSortedArrays(int[] A, int[] B) {
	    int m = A.length, n = B.length;
	    int l = (m + n + 1) / 2;
	    int r = (m + n + 2) / 2;
	    return (getkth(A, 0, B, 0, l) + getkth(A, 0, B, 0, r)) / 2.0;
	}

public double getkth(int[] A, int aStart, int[] B, int bStart, int k) {
	if (aStart > A.length - 1) return B[bStart + k - 1];            
	if (bStart > B.length - 1) return A[aStart + k - 1];                
	if (k == 1) return Math.min(A[aStart], B[bStart]);
	
	int aMid = Integer.MAX_VALUE, bMid = Integer.MAX_VALUE;
	if (aStart + k/2 - 1 < A.length) aMid = A[aStart + k/2 - 1]; 
	if (bStart + k/2 - 1 < B.length) bMid = B[bStart + k/2 - 1];        
	
	if (aMid < bMid) 
	    return getkth(A, aStart + k/2, B, bStart,       k - k/2);// Check: aRight + bLeft 
	else 
	    return getkth(A, aStart,       B, bStart + k/2, k - k/2);// Check: bRight + aLeft
}


// Time : O(log(m + n))



///Another solution

public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int index1 = 0;
    int index2 = 0;
    int med1 = 0;
    int med2 = 0;
    for (int i=0; i<=(nums1.length+nums2.length)/2; i++) {
        med1 = med2;
        if (index1 == nums1.length) {
            med2 = nums2[index2];
            index2++;
        } else if (index2 == nums2.length) {
            med2 = nums1[index1];
            index1++;
        } else if (nums1[index1] < nums2[index2] ) {
            med2 = nums1[index1];
            index1++;
        }  else {
            med2 = nums2[index2];
            index2++;
        }
    }

    // the median is the average of two numbers
    if ((nums1.length+nums2.length)%2 == 0) {
        return (float)(med1+med2)/2;
    }

    return med2;
}

class Solution:
    def duplicates(self, arr, n): 
    	hash_map = {}
    	dup_arr = []
    	for i in arr:
    	    value = hash_map.get(i)
    	    if value:
    	        if value == 1:
    	            dup_arr.append(i)
    	            hash_map[i]=2
    	    else:
    	        hash_map[i]=1
        if not dup_arr:
            return [-1]
        dup_arr.sort()
        return dup_arr

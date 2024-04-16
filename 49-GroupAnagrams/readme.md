# 49 Group Anagrams
## Intuition
- the angagrams has the same string after sorted(for example:"ate, eat, tea".After sorted, they are all "aet")
- Based on the same sorted string, we can add the string which is same after sorting.
- Using a defaultdictionary, and record the same sorted string as the value into the same key.Like dict["aet"] = ["ate", "eat", "tea"]
- After looping the whole string list, we can get the final dictionary and then change the values into list


## Complexity
- Time complexity:O(n * mlogm)
- m is the maxlegth which is one of string

## Space complexity:
- O(n*m) 
- n is the counts of the string list, m is the average length of the string 

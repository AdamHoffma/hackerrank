Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

#We'll have to loop through the array and multiply subarrays
#We'll keep a min counter and everytime a new product is larger replace min

I'm really struggling to understand exactly how this works.... but it replaces min and max as it loops

let res = -Number.MAX_VALUE    #this set the lowest value possible
let min = 1   I think that's to grab a ref to the original number out the gate
let max = 1   Same

for (let num of nums) {
    [min, max] = [                  Really interesting here, setting min and max to an array
        Math.min(num, min * num, max * num)  Would equal 2 Min is now now 2
        Math.max(num, min * num, max * num)  Same   for the next number which is 3             (3, 2 * 3, 2 * 3) Max is 6 min is 2  next number is -2  (-2, 2 * -2, 6 * -2) Max is -2 min is -12???


        I think everyone gets set to an array, and then we grab the max number from the array....
    ]
}
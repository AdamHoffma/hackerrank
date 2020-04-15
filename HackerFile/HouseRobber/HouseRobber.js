function rob(nums) {
    let arr = []
    let arr2 = []

    for (let i =0; i < nums.length; i++){
        if (i % 2 == 0) {
            arr.push(nums[i])
        }
        else if (i % 2 == 1) {
            arr2.push(nums[i])
        }
    }
    let even = arr.reduce((a, b) => a + b, 0)
    let odd = arr.reduce((a, b) => a + b, 0)
    return Math.max(even, odd)
}
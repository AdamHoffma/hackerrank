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

function rob(nums) {
    let solution = {}
    solution[nums.length] = 0
    solution[nums.length - 1] = nums[nums.length - 1]
    
    for (let i = nums.length-2; i >= 0; i--) {
      solution[i] = Math.max(nums[i] + solution[i + 2], solution[i+1])
      
    }
    return solution
  }
  
  console.log(rob([2, 1, 1, 2]))
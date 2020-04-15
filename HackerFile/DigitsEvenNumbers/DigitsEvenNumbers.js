function findNumbers(nums) {
    let result = 0
    nums.forEach(n => {
        if (n.toString().length % 2 == 0) {
            result += 1
        }
    })
    return result
}
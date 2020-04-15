var createTargetArray = function(nums, index) {
    let array = []
    let target = []
    
    for(let i = 0; i < nums.length; i++){
        array.push(nums[i])
    }
    for(let j = 0; j < index.length; j++){
        array.push(index[j])
        console.log(array)
    }
    for(let x = 0; x < array.length; x++){
        if (x == nums.length){
            break
        }
        target.splice(array[x + nums.length], 0, array[x])
    }
    return target
};
function fibonacci(n) {
  var a = 1, b = 0, temp
  ans = []
  
  while (n >= 1){
  ans.push(b)
  temp = a
  a = a + b
  
  b = temp
  n--
  }
  return ans
}

console.log(fibonacci(4))
function balancedStringSplit(s) {
    let balance = 0
    let count = 0
    s = [...s]
    console.log(s)
    s.forEach(i => {
      if (i == "L") {
        balance += 1
        console.log(balance)
      } else {
        balance -= 1
        console.log(balance)      
        }
        if (balance == 0) {
          count += 1
      }
    })
    return count
  }
  
  balancedStringSplit("RRRLLL")
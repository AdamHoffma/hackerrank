rotLeft = (a, d) => {
    let i = 0
    while (i < d) {
        a.push(a.unshift())
        i++
    }
    return a
}
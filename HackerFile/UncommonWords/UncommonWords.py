def uncommFromSentences(A, B):
    count = {}
    for word in A.split():
        count[word] = count.get(word, 0) + 1
    for word in B.split():
        count[word] = count.get(word, 0) + 1
    return [word for word in count if count[word] == 1]

print(uncommFromSentences("this is a sentence", "this is as well"))
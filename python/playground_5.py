def filter_by_length(words):
    result = list(filter(lambda word:len(word) >= 4, words))
    return result

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)
word = input().upper()

word_set = list(set(word))
cnt = []

for i in word_set:
    cnt.append(word_set.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_set[cnt.index(max(cnt))])

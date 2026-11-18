# ATTS 03-24 R ABDURASHIDOV ABDULAZIZ


import matplotlib.pyplot as plt
from collections import Counter

spam_score = 84.5
links = 8
name = 'Xat 101'
print(type(spam_score))
print(type(links))


email = {
    'spam_score': 84.5,
    'links': 8,
    'length': 84
}
print(email['spam_score'])


spam_score = 65
if spam_score > 70:
    print('Spam')
else:
    print('Spam emas')


def check_spam(spam_score, links):
    if spam_score > 70 or links > 5:
        return 'spam'
    else:
        return 'spam emas'

print(check_spam(65, 8))
print(check_spam(40, 2))


records = [
    {'score': 65, 'links': 8},
    {'score': 40, 'links': 2},
]
for r in records:
    print(check_spam(r['score'], r['links']))


group = [(65, 8), (40, 2), (80, 3), (30, 1), (90, 9),
         (55, 4), (75, 6), (85, 7), (20, 0), (60, 9)]
labels = [check_spam(score, links) for score, links in group]
counts = Counter(labels)
print(counts)

order = ['spam', 'spam emas']
values = [counts.get(k, 0) for k in order]

bars = plt.bar(order, values, color=['red', 'green'])
plt.bar_label(bars)
plt.title('Nechta xat spam')
plt.ylabel('Xatlar soni')
plt.yticks(range(0, max(values) + 2))
plt.savefig('spam_chart.png', dpi=150, bbox_inches='tight')
import sys
import editdistance
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
sents1 = [x.strip().split(',')[1] for x in f1.readlines()[1:]]
sents2 = [x.strip().split(',')[1] for x in f2.readlines()[1:]]
total = 0
lev_sum = 0
for sent1, sent2 in zip(sents1, sents2):
    lev_sum += editdistance.eval(sent1, sent2)
    total += 1

print("Mean Levenshtein Distance:", float(lev_sum)/total)

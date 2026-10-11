"""Independent Bernoulli attempts with constant success probability."""
import csv
import math
from pathlib import Path
def probability(p, n):
    if not 0 <= p <= 1 or not isinstance(n, int) or n < 0:
        raise ValueError('Require 0 <= p <= 1 and a nonnegative integer n')
    return 1 - (1-p)**n
def attempts_for_target(p, target=0.95):
    if not 0 < p < 1 or not 0 < target < 1:
        raise ValueError('Require probabilities strictly between 0 and 1')
    return math.ceil(math.log1p(-target) / math.log1p(-p))
if __name__ == '__main__':
    print(f'20 attempts, p=10%: {100*probability(.1,20):.4f}%')
    for p in [.1, .05, .02]:
        print(f'p={p:.0%}: {attempts_for_target(p)} attempts for >=95%')
    with (Path(__file__).parent / 'model-probabilities.csv').open('w', newline='', encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['p','attempts','probability_at_least_one_offer'])
        for p in [.1, .05, .02]:
            for n in range(151):
                w.writerow([p,n,probability(p,n)])

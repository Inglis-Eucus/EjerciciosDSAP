"""C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementa-
tions, from page 41, was the most efﬁcient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance ad-
vantages."""


def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k 
        k += 1
    if k * k == n:
        yield k 
    while 0 < k * k < n+1:
        if n % k == 0:
            yield n // k
        k -= 1



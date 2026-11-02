t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = input()
    q = input()

    freq1 = dict()
    freq2 = dict()

    # Count characters in numerator p
    for i in range(len(p)):
        freq1[p[i]] = freq1.get(p[i], 0) + 1

    # Count characters in denominator q
    for i in range(len(q)):
        freq2[q[i]] = freq2.get(q[i], 0) + 1

    flag = True

    # Cancel characters of q from p
    for ch in freq2:
        if freq1.get(ch, 0) < freq2[ch]:
            flag = False
            break

        freq1[ch] -= freq2[ch]

    # After cancellation, remaining characters must be exactly "six"
    if flag and freq1.get('s', 0) == 1 and freq1.get('i', 0) == 1 and freq1.get('x', 0) == 1:
        extra = 0

        for ch in freq1:
            if ch != 's' and ch != 'i' and ch != 'x':
                extra += freq1[ch]

        if extra == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
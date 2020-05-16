n = int(raw_input('n: '))
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1

    print n,
# 考拉兹猜想(英语:Collatz conjecture)，又称奇偶归一猜想，3n+ 1 猜想、冰雹猜想、角谷猜想、哈塞猜想、乌拉姆猜想或叙拉古猜想
# 对于每一个正整数，如果它是奇数，则对它乘 3 再加 1，如果它是偶数， 则对它除以 2，如此循环，最终都能够得到1
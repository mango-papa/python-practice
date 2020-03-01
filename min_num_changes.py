
def find_change(change, coins):
    result = [0] * (change + 1)
    for i in range(0, change + 1):
        min_coins = float('inf')
        for c in coins:
            if i == c:
                min_coins = 1
                break
            elif i > c:
                min_coins = min(min_coins, 1 + result[i - c])
        result[i] = min_coins
    return result[-1]

def find_change2(change, coins):
    result = [dict.fromkeys(coins, 0)] * (change + 1)
    for i in range(1, change + 1):

        n = float('inf')
        cc = dict.fromkeys(coins, float('inf'))

        for c in coins:
            if i == c:
                # reset dictionary and give c count 1
                n = 1
                cc = dict.fromkeys(coins, 0)
                cc[c] = 1
                result[i] = cc
                break
            elif i > c:
                print('A', i, result)
                if n > sum(result[i-c].values()) + 1:
                    n = sum(result[i-c].values()) + 1
                    print('B', result)
                    cc = result[i-c]
                    print('C', result)
                    cc[c] += 1
                    print('D cc is now ', cc)
        print('E i:{}, cc: {}, result {}'.format(i, cc, result))
        result[i] = cc
        print('F i:{}, cc: {}, result {}'.format(i, cc, result))
        print('')
    return result[-1]

def count_coins(d):
    return sum(d.values())
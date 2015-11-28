__author__ = 'roksevcnikar'

roman_stevke = [['m', 1000], ['d', 500], ['c', 100], ['l', 50], ['x', 10], ['v', 5], ['i', 1]]

def toRoman(n):
    try:
        n = int(n)
        if 0 < n < 4000:
            i = 0
            rn = ''
            while i < 7:
                ri = roman_stevke[i]
                ni = n / ri[1] % 10
                if ni < 4:
                    rn = rn + ri[0] * ni
                elif ni > 8:
                    rn = rn + ri[0] + roman_stevke[i - 2][0]
                elif ni == 4:
                    rn = rn + ri[0] + roman_stevke[i-1][0]
                else:
                    rn = rn + roman_stevke[i-1][0] + ri[0] * (ni % 5)
                i += 2
            return rn
    except :
        pass
    return 'no valid entry'

if __name__ == "__main__":
    # for i in range(1,3999) :
    #     print toRoman(i)
    print "Vnesi stevilo: "
    n = raw_input()
    print toRoman(n)
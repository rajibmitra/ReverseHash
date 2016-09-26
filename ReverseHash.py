class HashReverse:
    def __init__(self):
        self.letters = 'acdegilmnoprstuw'
        self.h = 7

# Function for reversing hash
    def reverseHash(self, n):


        #just reverse of the given algorithm
        # Int64 hash (String s) {
        # Int64 h = 7
        # String letters = "acdegilmnoprstuw"
        # for(Int32 i = 0; i < s.length; i++) {
        # h = (h * 37 + letters.indexOf(s[i]))
        # }
        # return h
        # }


        ans = ''
        while n > 0:
            i = n % 37
            try:
                ans += self.letters[i]          # Get that letter and append to ans
            except Exception as e:
                print('Hashed value invalid')
            n = int((n - i) / 37)

            if n == self.h:
                return ans[::-1]                # reversing produces string backwards
            if n < self.h:
                print('Hashed value invalid')


if __name__ == '__main__':
    test = HashReverse()
    print(test.reverseHash(930846109532517))    # we have got our answer i.e "lawnmower"
    print(test.reverseHash(680131659347))       # tested this value from question and answer matches the given string

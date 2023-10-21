class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_new = []
        t_new = []

        s_new = self.clean(s)
        t_new = self.clean(t)

        if s_new == t_new:
            return True
        return False

    def clean(self, strg):
        word = []
        new_strng =""
        countDown = 0
        print(strg)
        for i,e in enumerate(strg):
            countDown = 0
            if e == "#":
                if len(word)!=0:
                
                    print("Word popped", word.pop())
                continue

            else:
                print("Element being added", e)
                word.append(e)
        
        # for j in word:
        #     new_strng +=word[j]
        # print(new_strng)
        return word
        

s = "y#fo##f"
t = "y#f#o##f"
s1 = Solution()
print(s1.backspaceCompare(s,t))

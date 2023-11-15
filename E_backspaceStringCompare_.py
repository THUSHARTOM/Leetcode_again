# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s_new = []
#         t_new = []

#         s_new = self.clean(s)
#         t_new = self.clean(t)

#         if s_new == t_new:
#             return True
#         return False

#     def clean(self, strg):
#         word = []            # doesnt have to be a dictionary
#         new_strng =""
#         countDown = 0
#         print(strg)
#         for i,e in enumerate(strg):
#             countDown = 0
#             if e == "#":
#                 if len(word)!=0:
                
#                     print("Word popped", word.pop())
#                 continue

#             else:
#                 print("Element being added", e)
#                 word.append(e)
        
#         # for j in word:
#         #     new_strng +=word[j]
#         # print(new_strng)
#         return word
        

# s = "y#fo##f"
# t = "y#f#o##f"
# s1 = Solution()
# print(s1.backspaceCompare(s,t))

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(str, index):
            backspace = 0
            while index>=0:
                if backspace ==0 and str[index] != "#":
                    break
                elif str[index] == "#":
                    backspace +=1
                else:
                    backspace-=1
                index-=1       
            return index

        t_pointer = len(t) -1
        s_pointer = len(s) -1

        while t_pointer>=0 and s_pointer>=0:
            t_pointer = nextValidChar(t,t_pointer)
            print("T == ", t[t_pointer])
            s_pointer = nextValidChar(s,s_pointer)
            print("S == ", s[s_pointer])
           
            char_s = s[s_pointer] if s_pointer>=0 else ""
            char_t = t[t_pointer] if t_pointer>=0 else ""
            if char_s != char_t:
                return False

            t_pointer -=1
            s_pointer -=1
            print("T_pointer", t_pointer)
            print("s_pointer", s_pointer)
        return True

    



s = Solution()
print(s.backspaceCompare("ab##", "c#d#"))
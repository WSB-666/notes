from collections import Counter

# L 217 存在重复元素
# 方法一
def quchong(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# 方法二
def quchong1(nums):
    return len(set(nums)) != len(nums)

# L 242 有效的字母异位词
def yiwei(s,t):
    return sorted(s) == sorted(t)


def yiwei2(s,t):
    return Counter(s) == Counter(t)

# L 125 验证回文串
import re
def isPalindrome(s):
    result = re.sub(r'[^a-z0-9]','',s.lower())
    return result == result[::-1]

def isPalindrome1(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True 

def isPalindrome3(s):
    result = ''.join(c for c in s.lower() if c.isalnum() and c.isalpha())
    return result == result[::-1]

if __name__ == "__main__":
    # nums = list(map(int,input().split()))
    # print(quchong(nums),quchong1(nums))
    # s,t = input().split()
    # print(yiwei(s,t),yiwei2(s,t))
    s = input()
    print(isPalindrome(s))

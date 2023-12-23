from collections import deque
import re

def check_palindrome(word: str) -> bool:
  word = re.sub(r'[^A-Za-z]', '', word)
  dq = deque([*word])
  while len(dq) > 1:
    if not dq.popleft().lower() == dq.pop().lower():
      return False

  return True

print(check_palindrome('A man, a plan, a canal – Panama'))

print(check_palindrome('my 452342 test'))

print(check_palindrome('Aa'))

print(check_palindrome('C'))

print(check_palindrome('ab777 777234234234ba'))

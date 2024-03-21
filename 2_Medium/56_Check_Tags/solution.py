from collections import deque

def CheckDOM(strParam):
  queue_tag = deque()
  idx = 0
  length = len(strParam)
  #save tags in deque_tag
  while idx < length:
    if strParam[idx] == '<':
      end_idx = idx+1
      if end_idx == length:
        break
      current_tag = ""
      while end_idx < length and strParam[end_idx] != '>':
        current_tag += strParam[end_idx]
        end_idx += 1
      if end_idx < length and strParam[end_idx] == '>':
        queue_tag.append(current_tag)
    if idx < end_idx:
      idx = end_idx
    else:
      idx += 1
  count_all = 0
  count_open_tag = 0
  count_closed_tag = 0
  for tag in queue_tag:
    count_all += 1
    if tag[0] == '/':
      count_closed_tag += 1
    else:
      count_open_tag += 1
  if count_all%2 ==1 or count_open_tag != count_closed_tag:
    return False
  empty_deque = deque()
  incorrect_tags = 0
  first_incorrect = ""
  while queue_tag != empty_deque:
    left_tag = queue_tag.popleft()
    right_tag = queue_tag.pop()
    if left_tag == right_tag[1:] and right_tag[0] == '/':
      continue
    else:
      incorrect_tags += 1
      if incorrect_tags ==1:
        first_incorrect = left_tag
  if incorrect_tags == 1:
    return first_incorrect
  if incorrect_tags > 1:
    return False
  return True

print(CheckDOM("<d><div>Hello</d></div>"))
print(CheckDOM("<d><div>Hello</div></d>"))
print(CheckDOM("<em><div>Hello</d></div>"))
print(CheckDOM("<em><div>Hello</d></em>"))


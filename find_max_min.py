def find_max_min(arg):
  ans = []
  max_num = max(arg)
  min_num = min(arg)
  if min_num == max_num:
    length = len(arg)
    ans.append(length)
  else:
    ans.append(min_num)
    ans.append(max_num)
  return ans

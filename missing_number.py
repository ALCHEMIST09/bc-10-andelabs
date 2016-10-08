def find_missing(list1, list2):
    longer = []
    shorter = []
    if len(list1) > len(list2):
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1
    missing = [x for x in longer if x not in shorter]
    if len(missing) == 0:
      return 0
    return missing.pop()

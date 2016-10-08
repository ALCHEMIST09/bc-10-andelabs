def words(arg):
    result = {}
    parts = arg.split()
    if len(parts) == 1:
        result[parts[0]] = 1
        return result
    else:
        for item in parts:
            if item.isdigit():
                item = int(item)
            result[item] = parts.count(str(item))
        return result

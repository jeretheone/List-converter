def convert(lists):
    lists = str(lists)
    lists = lists.replace("[", "")
    lists = lists.replace("]", "")
    lists = lists.replace("'", "")
    return lists

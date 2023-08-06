def strformat(the_list, format=False,level=0):
    """This function takes in a list and then identifies if any items within the list are also lists or not and then prints each item separately."""
    for item in the_list:
        if isinstance(item, list):
            strformat(item, format, level+1)
        else:
            if format:
                for tab in range(0,level):
                    print('\t',end="")
            print(item)

# movies = [
#     "All the president's men",[1982, "Jason Burrow"],"The Godfather",[1987,["Al Pacino","Percy Jackson","Roger Stone"]]
# ]

# nester(movies,True,2)
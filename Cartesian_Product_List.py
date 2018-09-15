"""
Given list of lists get their cartesian product
Example:
Input:[[1,2],[3,4],[5,6]]
Output: [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

"""

def cartesian_product(arr_list):
    if not ar_list:
        yield ()
    else:
        for a in arr_list[0]:
            for prod in product(arr_list[1:]):
                yield (a,)+prod

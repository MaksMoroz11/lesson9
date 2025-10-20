# from random import randint as random

#
# # 1
# summa, count = 0, 0
# while (x := int(input())) != 0:
#     summa += x
#     count += 1
# print(summa / (count if count > 0 else 1))
#
#
# # 2
# def min_val_in_list(_list):
#     min_val = _list[0]
#     for i in _list:
#         if i < min_val:
#             min_val = i
#     return min_val
#
#
# print(min_val_in_list(list1))
#
#
# # 3
# def list_with_random_vals():
#     return [random(1, 10) for i in range(10)]
#
#
# print(list_with_random_vals())
#
#
# # 4
# def sum_lists(_list, _list2):
#     return _list + _list2
#
#
# print(sum_lists(list1, list1))
#
#
# # 5
# def pop_val_in_list(_list, n):
#     return [_list[i] for i in range(len(_list)) if n != i]
#
#
# print(pop_val_in_list(list1, 2))
#
# print()


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -12]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 21]


# 6

# def uniq_elms_in_lists(list1, list2, list3):
#     set1, set2, set3 = set(list1), set(list2), set(list3)
#     return list((set1 ^ set2) | (set2 ^ set3) | (set1 ^ set3))

#
# def uniq_elms_in_lists(lists):
#     uniq_elms = []
#     for i in range(len(lists)):
#         for k in lists[i]:
#             elm = None
#             for j in range((0 if len(lists) == i+1 else i+1), (1 if len(lists) == i+1 else len(lists))):
#                 elm = k
#                 if k in lists[j]:
#                     elm = None
#                     break
#             if elm is not None:
#                 uniq_elms.append(elm)
#     return uniq_elms
#
#
# print( uniq_elms_in_lists( [list1, list2, list3] ) )

students = [
    [1, 23, 24, 100],
    [24, 23, 15, 50],
    [80, 76, 54, 24]
]

for student in students:
    print(student[1], end=" ")
def quick_sort(a_list):
    if len(a_list) <= 1:        
        return a_list
    else:
        left_mark = 1
        right_mark = len(a_list) - 1
        while left_mark < right_mark:
            while left_mark < len(a_list) and a_list[left_mark] < a_list[0]:
                left_mark += 1
            while a_list[right_mark] > a_list[0]:
                right_mark -= 1
            if left_mark < right_mark:
                a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
            else:
                break        
        a_list[0], a_list[right_mark] = a_list[right_mark], a_list[0]
        left_list, right_list = [], []
        for i in range(right_mark):
            left_list.append(a_list[i])
        for j in range(right_mark + 1, len(a_list)):
            right_list.append(a_list[j])
        return quick_sort(left_list) + [a_list[right_mark]] + quick_sort(right_list)
        
import random
a=[]
for i in range(20):
    a.append(random.randrange(1000))
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(a)
print(quick_sort(a))
        
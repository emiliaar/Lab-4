from itertools import *

STOCK = [
  {'Обозначение': 'r', 'Размер': 3, 'Очки': 25},
  {'Обозначение': 'p', 'Размер': 2, 'Очки': 15},
  {'Обозначение': 'a', 'Размер': 2, 'Очки': 15},
  {'Обозначение': 'm', 'Размер': 2, 'Очки': 20},
  {'Обозначение': 'i', 'Размер': 1, 'Очки': 5},
  {'Обозначение': 'k', 'Размер': 1, 'Очки': 15},
  {'Обозначение': 'x', 'Размер': 3, 'Очки': 20},
  {'Обозначение': 't', 'Размер': 1, 'Очки': 25},
  {'Обозначение': 'f', 'Размер': 1, 'Очки': 15},
  {'Обозначение': 'd', 'Размер': 1, 'Очки': 10},
  {'Обозначение': 's', 'Размер': 2, 'Очки': 20},
  {'Обозначение': 'c', 'Размер': 2, 'Очки': 20}
]


def res(CAPACITY):
    ITEMS_AMOUNT = len(STOCK)
    all_points = 15
    symbols = [''] + [item['Обозначение'] for item in STOCK]
    size = [0] + [item['Размер'] for item in STOCK]
    points = [0] + [item['Очки'] for item in STOCK]
    table = [[0 for _ in range(CAPACITY+1)] for _ in range(ITEMS_AMOUNT+1)]
    took = [['' for _ in range(CAPACITY+1)] for _ in range(ITEMS_AMOUNT+1)]

    for item in range(ITEMS_AMOUNT+1):
        for cells in range(CAPACITY+1):
            current_points = points[item]
            prev_points = table[item-1][cells]
            prev_points_at_offset = table[item-1][cells-size[item]]
            if item == 0 or cells == 0:
                table[item][cells] = 0
            elif cells >= size[item] and current_points + prev_points_at_offset > prev_points:
                    table[item][cells] = current_points + prev_points_at_offset
                    took[item][cells] = symbols[item]*size[item] + took[item-1][cells-size[item]]
            else:
                table[item][cells] = prev_points
                took[item][cells] = took[item-1][cells]

    really_took = took[-1][-1]
    for i, symb in enumerate(symbols):
        if symb in really_took:
            all_points += points[i]
        else:
            all_points -= points[i]
    return really_took, all_points

really_took, all_points = res(CAPACITY=2*4)
print([really_took[0]], [really_took[1]])
print([really_took[2]], [really_took[3]])
print([really_took[4]], [really_took[5]])
print([really_took[6]], [really_took[7]])
print('Итоговые очки выживания:', all_points)


#Доп задание №1
all_points = res(CAPACITY=7)[1]
if all_points <= 0:
    print('Для случая с инвентарём в 7 ячеек решения нет, так как в итоге остается максимум', all_points, 'очков выживания')


#доп задание №2
ITEMS_AMOUNT = len(STOCK)
symbols = [''] + [item['Обозначение'] for item in STOCK]
size = [0] + [item['Размер'] for item in STOCK]
points = [0] + [item['Очки'] for item in STOCK]

CAPACITY = 2 * 4
sum_points = sum(points)

max_items_amount = 0
sort_size = sorted(size[1:])
for num in range(1, ITEMS_AMOUNT+1):
    if sum(sort_size[:num]) <= CAPACITY:
        max_items_amount = num
    else:
        break

min_items_amount = 0
sort_points = sorted(points[1:])[::-1]
for num in range(1, ITEMS_AMOUNT+1):
    sum_max_points = sum(sort_points[:num])
    if (15 + sum_max_points) - (sum_points - sum_max_points) > 0:
        min_items_amount = num
        break

extra_task_2 = set()
for k in range(min_items_amount, max_items_amount+1):
    for combination in permutations(symbols[1:], k):
        comb = ''
        all_points = 15
        points_of_combination = 0
        space = 0
        for symb in combination:
            idx = symbols.index(symb)
            points_of_combination += points[idx]
            comb += symb * size[idx]
        all_points += points_of_combination
        if len(comb) <= 8 and all_points - (sum_points - points_of_combination) > 0:
            extra_task_2.add(comb)
print(extra_task_2)
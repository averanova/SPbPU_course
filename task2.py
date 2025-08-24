# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep=','):
    part1 = group1.split(sep)
    part2 = group2.split(sep)
    common_part = sorted(set(part for part in part1 if part in part2))

    return common_part


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, sep='|')
print(common_participants)

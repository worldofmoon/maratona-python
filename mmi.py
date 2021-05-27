t = int(input())

lines = []
for _ in range(t):
    grades = [int(grade) for grade in input().split()]

    lowest_grade = min(grades)
    greatest_grade = max(grades)
    uniform = len(set(grades)) == 1

    lines.append(f'{lowest_grade} {greatest_grade}')
    lines.append('S' if uniform else 'N')

print('\n'.join(lines), end='')

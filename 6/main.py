part1 = 0
part2 = 0
for group in open("input.txt").read().split('\n\n'):
    answers = [set(x) for x in group.split('\n')]
    part1 += len(answers[0].union(*answers[1:]))
    part2 += len(answers[0].intersection(*answers[1:]))

print(f"Part 1 answer: {part1}")
print(f"Part 2 answer: {part2}")

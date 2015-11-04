import fileinput

lines = fileinput.input()
N = int(lines[0])
A = list(set(map(int, lines[1].split(" "))))
max_item = max(A)
while max_item in A:
    A.remove(max_item)
print(max(A))

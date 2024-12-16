with open("input.txt") as file:
    lines = file.readlines()

for index, offset in enumerate([0, 10000000000000]):
    total = 0
    for i in range(0, len(lines), 4):
        a = lines[i].strip().split('+')
        a = [int(a[1].split(',')[0]), int(a[2])]
        b = lines[i + 1].strip().split('+')
        b = [int(b[1].split(',')[0]), int(b[2])]
        x = lines[i + 2].strip().split('=')
        x = [offset + int(x[1].split(',')[0]), offset + int(x[2])]

        row1 = [a[0], b[0], x[0]]
        row2 = [a[1], b[1], x[1]]

        for j in range(2, -1, -1):  # Normalizing row1
            row1[j] /= row1[0]
        for j in range(2, -1, -1):  # Adjusting row2 based on row1
            row2[j] -= row2[0] * row1[j]
        for j in range(2, 0, -1):  # Normalizing row2
            row2[j] /= row2[1]
        for j in range(2, 0, -1):  # Adjusting row1 based on row2
            row1[j] -= row1[1] * row2[j]

        if abs(row1[2] - round(row1[2])) < 0.001 and abs(row2[2] - round(row2[2])) < 0.001:
            total += (3 * row1[2] + row2[2])

    print("PART " + str(index + 1) + " SOLUTION " + str(int(total)))

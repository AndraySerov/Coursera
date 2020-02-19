with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
    with open('new_file.txt', 'w') as nf:
        for line in reversed(lines):
            nf.write(line)

'''
#correct version from professeur
lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))
#few other versions
with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
    fw.writelines(fr.readlines()[::-1])


print(*reversed(open("sample.txt").readlines()), sep="")
'''

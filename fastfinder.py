import sys

if len(sys.argv) != 6:
    print('Invalid number of arguments')
    sys.exit(2)

a = sys.argv
fasta = a[1]
fai = fasta + '.fai'
seq = a[2]
start = int(a[3])
end = int(a[4])
out = a[5]

f1 = open(fai, 'r')
f2 = open(fasta, 'r')
f3 = open(out, 'w')
for line in f1:
    ln = line.strip()
    li = ln.split()
    if li[0] == seq:
        p = int(li[2]) + start + int(start/int(li[3])) * (int(li[4]) - int(li[3])) - 1
        end1 = end + int((end - start)/int(li[3])) * (int(li[4]) - int(li[3])) - 1
        f2.seek(p)
        res = f2.read(end1 - start)
name = out.split('.')
res = '>' + name[0] + '\n' + res + '\n'
f3.write(res)
f1.close()
f2.close()
f3.close()

#break
while True:
    kata = input("masukkan katanya:")
    if kata == "berhenti":
        print("kamu menyuruh berhenti:")
        break
    print("kamu mengetik", kata)

#continue
i = 0 
for i in range(5):
    if i == 3:
        continue
    print(i)

i = 0
for i in range(10):
    if i == 22:
        break
    print(i)

#nested loop

for i in range (5):
    for j in range (3):
        print (i,j)


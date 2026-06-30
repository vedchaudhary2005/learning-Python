import os

os.makedirs("table", exist_ok=True)

def genTable(n):
    table = ""
    for i in range(1, 11):
        table +=f"{n} X {i} = {n*i}\n"

        with open(f"table/tables_{n}.txt", "w") as f:
            f.write(table)

for i in range (2, 21):
    genTable(i)



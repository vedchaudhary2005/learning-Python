word = "donkey"
with open("file.txt", "r")as f:
    content = f.read()

contentNew = content.replace("donkey", "#######")

with open("file.txt", "w")as f:
    content = f.write(contentNew)
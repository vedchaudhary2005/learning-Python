f = open("poem.txt", "r")
content = f.read()
if("winkle Twinkle" in content):
    print("The Word twinkle preset in the sentence")
f.close() 
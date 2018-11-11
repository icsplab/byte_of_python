import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

f.close()

txt = io.open("abc.txt", encoding="utf-8").read()

print txt

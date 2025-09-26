s = "hello world"
ch = "o"
index = 4
remove_chars = "ol"

result1 = s.replace(ch, "", 1)
result2 = s.replace(ch, "")
result3 = s[:index] + s[index+1:]
result4 = s.translate(str.maketrans("", "", remove_chars))

print("Original String:", s)
print("Remove first occurrence of", ch, ":", result1)
print("Remove all occurrence of", ch, ":", result2)
print("Remove character at index", index, ":", result3)
print("Remove characters", remove_chars, ":", result4)

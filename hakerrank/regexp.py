

# examples
#floating points
print re.match(r"^[-+]?[0-9]*\.[0-9]+$",temp)

# re.split()
print '\n'.join(i for i in re.split('[.,]', raw_input()) if len(i)> 0)

# groups 
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)


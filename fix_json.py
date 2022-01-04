import os
import io
xs = open("test.json", 'w', encoding='utf-8')
xs.write('[')

trailing = ""
with open("european-20181028.json", encoding='utf-8-sig') as f:
    for line in f:
        xs.write(trailing)
        xs.write(line)
        if line.strip() == '}':
            trailing = ","
        else:
            trailing = ""
xs.write("]")
xs.flush()
xs.close()
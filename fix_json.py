import os
import io
xs = open("test.json", 'w', encoding='utf-8')
xs.write('[')
cnt = 0

trailing = ""
with open("european-20181028.json", encoding='utf-8-sig') as f:
    for line in f:
        xs.write(trailing)
        xs.write(line)
        if line.strip() == '}':
            trailing = ","
            cnt += 1
            if cnt > 500:
                break
        else:
            trailing = ""
xs.write("]")
xs.flush()
xs.close()
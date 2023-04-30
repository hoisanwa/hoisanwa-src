from glob import glob

inits = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
entries = sorted(glob("./Hoisanwa/words/*/*.md"))
topics = sorted(glob("./Hoisanwa/topics/*.md"))

inits_exist = [init for init in inits if any("/"+init+"/" in entry for entry in entries)]

with open("Hoisanwa/Home.md", 'w') as f:
    f.write("# 首页 / Home\n\n")

    f.write("## 专题 / Topics\n\n")
    for topic in topics:
        f.write(f"- [[{topic.split('/')[-1].split('.')[0]}]]\n")
    f.write("- [[台山话文库]]")
    f.write("\n")
    
    f.write("## 索引 / Index\n\n")
    f.write(f"现时收录条目：{len(entries)} 条。\n\n")
    for init in inits:
        if init in inits_exist:
            f.write(f"### {init}\n\n")
            s = ""
            for i, entry in enumerate(entries):
                if "/"+init+"/" in entry:
                    if i!=0 and i % 10 == 0:
                        s += f"\n[[{entry.split('/')[-1].split('.')[0]}]] "
                    else:
                        s += f"[[{entry.split('/')[-1].split('.')[0]}]] "
            f.write(s + "\n\n")

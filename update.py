from glob import glob

# list 26 alphebets
inits = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
entries = glob("./Hoisanwa/words/*/*.md")
inits_exist = [init for init in inits if any("/"+init+"/" in entry for entry in entries)]
with open("Hoisanwa/Home.md", 'w') as f:
    f.write("# 首页 / Home\n\n")
    f.write("## 索引 / Index\n\n")

    for init in inits:
        if init in inits_exist:
            f.write(f"### {init}\n\n")
            s = ""
            for i, entry in enumerate(entries):
                if "/"+init+"/" in entry:
                    if i==0 or i % 10 != 0:
                        s += f"[[{entry.split('/')[-1].split('.')[0]}]] "
                    else:
                        s += f"\n[[{entry.split('/')[-1].split('.')[0]}]] "
            f.write(s + "\n\n")
        


# with open("Hoisanwa/Home.md", 'w') as f:
#     f.write("# Home\n\n")

#     for init in inits:
#         f.write(f"## {init}\n")
#         for entry in entries:
#             if "/"+init+"/" in entry:
#                 filename = entry.split("/")[-1].split(".")[0]
#                 f.write(f"[[{filename}]]\n")
#         f.write("\n\n")
    
                

        
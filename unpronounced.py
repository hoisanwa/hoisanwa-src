from glob import glob

entries = sorted(glob("./Hoisanwa/words/*/*.md"))
audios = sorted(glob("./Hoisanwa/audios/*.m4a"))


entries = [entry.split('/')[-1].split('.')[0] for entry in entries]
audios = [audio.split('/')[-1].split('.')[0].split("-")[0] for audio in audios]

for e in sorted(set(entries) - set(audios)):
    print(e + "-台城-男")
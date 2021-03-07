


from zipfile import ZipFile
from tqdm import tqdm
import os
from sys import exit

path = r"PATHTOFOLDER"
os.chdir(path)

wordlist = "PASSWORDLIST.txt"
zip_file = "LOCKEDFOLDER.zip"

n_words = len(list(open(wordlist, encoding="utf-8", errors='ignore')))
print("Total passwords to test:", n_words)

with open(wordlist, encoding="utf-8", errors='ignore') as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        pw=(word.strip())
        try:
            ZipFile(zip_file).extractall(path, pwd=pw.encode())
        except:
            continue
        else:
            print("Password found:", pw)
            exit(0)
print("Password not found, try other wordlist.")


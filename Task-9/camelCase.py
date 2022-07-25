#  HackerRank CamelCase
def camelCase(s):
    count=1
    for i in range(len(s)):
        if s[i].isupper():
            count+=1
    return count
if __name__ == "__main__":
    s=input()
    print(camelCase(s))
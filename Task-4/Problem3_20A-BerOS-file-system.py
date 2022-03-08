# CodeForces : 20A BerOS file system
if __name__ == "__main__":
    path=input()
    str= (path.split("/"))
    str=list(filter(None, str))
    str="/"+"/".join(str)
    print(str)
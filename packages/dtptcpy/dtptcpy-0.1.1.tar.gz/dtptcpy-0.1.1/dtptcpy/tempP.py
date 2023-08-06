

def read():
    try:
        with open("temp","r") as f:
            port = f.readline()
            if port.isdigit():
                if int(port)<65535:
                    return int(port)
    except:
        ...
    write(23331)
    return 23331
def write(port:int):
    with open("temp","w") as f:
        f.write(str(port))


if __name__=="__main__":
    b=read()
    print(b)
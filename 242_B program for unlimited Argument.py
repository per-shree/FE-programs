#program for unlimited Argument
def person(*name):
    for name in name:
        print(f"Hello {name}.")


person("Shree","Anuj","Sudhanshu","Sankarna")
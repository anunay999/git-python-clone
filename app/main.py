import sys
import os
import zlib
import hashlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Intialized git directory")
    elif command == "cat-file":
        param, hash = sys.argv[2], sys.argv[3]
        if param == '-p':
            with open(f".git/objects/{hash[:2]}/{hash[2:]}", "rb") as f:
                compressed = f.read()
                content = zlib.decompress(compressed).split(b'\0')[1].decode('utf-8')
                print(content, end="")
    elif command == "hash-object":
        param, file = sys.argv[2], sys.argv[3]
        if param == '-w':
            with open(f"{file}", "rb") as f:
                content = f.read()
                header = f'blob {len(content)}\0'.encode()
                content = header + content
                hash = hashlib.sha1(content).hexdigest()
                os.makedirs(f".git/objects/{hash[:2]}",exist_ok=True)
                with open(f".git/objects/{hash[:2]}/{hash[2:]}", "wb") as wb:
                    wb.write(zlib.compress(content))
                print(hash)
    elif command == "ls-tree":
        param, hash = sys.argv[2], sys.argv[3]
        if(param == '--name-only'):
            with open(f".git/objects/{hash[:2]}/{hash[2:]}", "rb") as f:
                data = zlib.decompress(f.read())
                _, binary_data = data.split(b'\x00', maxsplit=1)
                while binary_data:
                    mode, binary_data = binary_data.split(b'\x00', maxsplit=1)
                    _, name = mode.split()
                    binary_data = binary_data[20:]
                    print(name.decode('utf-8'))


    else:
        raise RuntimeError(f"Unknown command #{command}")
    



if __name__ == "__main__":
    main()

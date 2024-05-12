import sys
import os
import zlib


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
                compressed = zlib.compress(content)
                print(compressed, end="")

    else:
        raise RuntimeError(f"Unknown command #{command}")
    



if __name__ == "__main__":
    main()

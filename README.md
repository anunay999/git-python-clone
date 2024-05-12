
# Python Git Clone

This project is a simplified version of Git implemented in Python. It allows basic Git operations such as initializing a repository, hashing objects, reading file contents, writing tree structures, and committing changes.

## Features

- **Initialize a repository**: Set up a new Git-like repository.
- **Hash objects**: Create a hash for files (blobs) and directories (trees).
- **Read objects**: Extract and display the contents of stored objects.
- **Write tree**: Recursively hash the contents of a directory.
- **Commit changes**: Record changes to the repository with commit objects.

## Installation

No installation is necessary beyond having Python installed on your system. This script uses Python's standard libraries.

## Usage

Navigate to the directory where you want to use this script and execute the desired commands.

### Commands

- **init**
  - Initializes a new repository.
  - Example: `git.sh init`
  
- **cat-file**
  - Prints the contents of an object based on its hash.
  - Parameters:
    - `-p`: Specifies that the content should be printed.
    - `hash`: The hash of the object to retrieve.
  - Example: `git.sh  cat-file -p 1a2b3c4d`

- **hash-object**
  - Hashes a file and optionally writes it to the object storage.
  - Parameters:
    - `-w`: Indicates the blob should be written to the object storage.
    - `file`: The path to the file to hash.
  - Example: `git.sh  hash-object -w example.txt`

- **ls-tree**
  - Lists the contents of a directory tree based on its hash.
  - Parameters:
    - `--name-only`: List only the names of the contents.
    - `hash`: The hash of the tree to list.
  - Example: `git.sh ls-tree --name-only 1a2b3c4d`

- **write-tree**
  - Writes a tree object from the contents of the current directory.
  - Example: `git.sh write-tree`

- **commit-tree**
  - Creates a commit object.
  - Parameters:
    - `tree_sha`: The SHA-1 hash of the tree you are committing.
    - `parent_sha`: The SHA-1 hash of the parent commit.
    - `message`: The commit message.
  - Example: `git.sh commit-tree 1a2b3c4d -p 2b3c4d5e -m "Initial commit"`

### Development

You can extend this script to support more complex Git operations such as branching, merging, and remote synchronization.

## Understanding the Operations

- **Blob and Tree Objects**: Files are hashed and stored as blobs. Directories are represented as trees, which are also hashed and contain pointers to blobs or other trees.
- **Commit Objects**: Commits point to tree objects and link back to previous commits, forming the history of changes.

This tool simulates the core components of Git using Python and provides a basic understanding of how Git internally manages version control.

## Resources

- https://benhoyt.com/writings/pygit/
- https://blog.meain.io/2023/what-is-in-dot-git/
- https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

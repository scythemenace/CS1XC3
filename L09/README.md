# Student-Course Management System (Lab 9)

* Date: 2023-03-30
* Author: Ankur Pandey

## Table of Contents

- [Description](#description)
- [Installation Instructions](#installation-instructions)
- [Configuration Instructions](#configuration-instructions)
- [Operating Instructions](#operating-instructions)
- [Troubleshootin](#troubleshooting)
- [Changelog](#changelog)

## Description


Developed for CS1XC3 Lab_09, this software package aims to provide users with a set of tools and functions for managing Markdown, LaTeX and Makefiles. This package shows how to use these tools for effective documentation and software management. 

## Installation Instructions

To install the software package, follow these steps:

1. Bare clone the repository to your local machine: `git clone --bare git://github.com/username/repo.git`
2. Navigate to the bare cloned repository: `cd repo.git`
(Replace `<REPO_NAME>` with the actual repository name)
3. Create a new remote repository on GitHub or GitLab etc. and make sure it is empty (i.e., do not initialize it with a README or .gitignore file).
4. Push the bare cloned repository to the new remote repository: `git push --mirror <REMOTE_URL>`
5. Remove the local bare cloned repository: `cd .. && rm -rf repo.git`
6. Clone the new repository to your local machine: `git clone <REMOTE_URL>`




## ⚙️ Configuration Instructions

Make sure your system has the necessary components installed before configuring the software:

- LaTeX
- Doxygen
- Git

## Operating Instructions

1. Comply with the setup and setting guidelines.
2. Execute the make Doxyfile command to compile files, establish directories, and produce documentation using Doxygen: `make Doxyfile`
3. This will create a Doxyfile in the project's root directory.
4. After that, modify the Doxyfile as needed.
5. Use 'make all' to create the documentation by running the Makefile once more: `make all`
6. This will produce the documentation and build files.
7. The documentation directory will contain the generated documentation in the form of HTML files and the build will the contain the source files.
8. Open the "index.html" file in the "html" folder under the "doc" directory to examine the generated documentation.
9. Execute the following program: `./Build/main`
10. The program will instantly create the course "Basics of Mathematics" (MATH101) and sign up 20 randomly selected students for it.
11. The program prints the course information, followed by the top student and the list of passing students.

## Troubleshooting

If you experience problems with the software's download or use, please double-check the following:

If you experience problems with the software's download or use, please double-check the following:

1. Verify that every prerequisite has been correctly loaded.
2. Verify that you are in the right directory and that the repository has been properly cloned.
3. Verify that the Makefile is set correctly.
4. Ensure that a C compiler, such as GCC, is loaded on your system.
5. Before attempting to execute the program, make sure you have cloned the repository and completed the compilation process.
6. Look for compilation errors or warnings in the supplied code.

If you still have issues, please create an issue on the Github repository, and we will try to help you as soon as possible.

## Changelog

### 2023-03-28

- Initial release
- Added Makefile and LaTeX functionalities
- Initial release with student and course management functionality.

### 2023-03-30

- Made changes to the Doxygen documentation.
- Added doxycomments to the src folder files.
- Made the README.md file and updated the Doxyfile to include the README.md file.

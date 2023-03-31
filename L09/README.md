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


This software package is designed for CS1XC3 Lab09, aiming to provide users with a set of tools and functionalities related to Markdown, LaTeX, and Makefile management. The package demonstrates the usage of these tools for effective documentation and software management.

## Installation Instructions

To install the software package, follow these steps:

1. Bare clone the repository to your local machine: `git clone --bare git://github.com/username/repo.git`
2. Navigate to the bare repository directory: `cd repo.git`
(Replace `<REPO_NAME>` with the actual repository name)
3. Create a new remote repository on a platform like GitHub or GitLab, and make sure it is empty (i.e., do not initialize it with a README or .gitignore file).
4. Push the local bare repository to the new remote repository: `git push --mirror <REMOTE_URL>`
5. Remove the local bare repository: `cd .. && rm -rf repo.git`
6. Clone the new repository to your local machine: `git clone <REMOTE_URL>`




## ⚙️ Configuration Instructions

To configure the software, ensure that you have the following prerequisites installed on your system:

- LaTeX
- Doxygen
- Git

## Operating Instructions

1. Follow the installation and configuration instructions.
2. Run the Makefile to compile files, create directories, and generate documentation using Doxygen: `make Doxyfile`
3. This will generate a Doxyfile in the root directory of the project.
4. Then make the desired changes to the Doxyfile.
5. Run the Makefile again to generate the documentation: `make all`
6. This will create two directories documentation and build. 
7. The documentation directory will contain the generated documentation in the form of HTML files and the build will the contain the source files.
8. To view the generated documentation, open the 'index.html' file in the 'html' folder under the 'doc' directory.
9. Then run the program: `./Build/main`
10. The program will automatically generate a course named "Basics of Mathematics" (MATH101) and enroll 20 random students in the course.
11. The program will then print the course information, followed by the top student and the list of passing students.

## Troubleshooting

If you encounter issues during the installation or operation of the software, please check the following:

1. Ensure that all prerequisites are properly installed.
2. Check that the repository is cloned correctly and you are in the correct directory.
3. Make sure the Makefile is properly configured.
4. Ensure that you have a C compiler installed on your system, such as GCC.
5. Make sure that you have cloned the repository and compiled the program before trying to run it.
6. Check the provided code for any compilation errors or warnings.

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

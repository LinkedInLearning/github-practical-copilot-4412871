# Practical GitHub Copilot
This is the repository for the LinkedIn Learning course Practical GitHub Copilot. The full course is available from [LinkedIn Learning][lil-course-url].

![Practical GitHub Copilot][lil-thumbnail-url] 

Copilot–a paid service from GitHub–is revolutionizing the way code is written. According to reports from developers who use it, a vast majority feel more productive and can perform repetitive tasks almost twice as fast. If you're interested in learning how to solve problems with Copilot and become a more efficient developer, join instructor Ray Villalobos in this hands-on course as he shows you not just how to use Copilot to find the best solutions to concrete code problems, but how to make it work best in specific contexts. From setup to navigating the tools to refining the results, Ray demonstrates the practical applications of Copilot’s powerful features.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

## Installing
1. To use these exercise files, you must have the following installed:
	- [list of requirements for course]
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.
3. [Course-specific instructions]


### Instructor

Ray Villalobos 
                            
Author, Multimedia Developer

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/ray-villalobos).

[lil-course-url]: https://www.linkedin.com/learning/practical-github-copilot?dApp=59033956&leis=LAA
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQEVYkOcM5jKsQ/learning-public-crop_288_512/0/1686860280439?e=2147483647&v=beta&t=OQFBTMq5-PXArFGiBAIus3OK_EPIP1pKho5jLCXHJiI

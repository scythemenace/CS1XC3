#include <stdlib.h> 
#include <stdio.h>
#include <string.h>
#include "time.h"
#include "course.h"
/**
 * @file main.c
 * @author Ankur Pandey
 * @date 2023-03-30
 * @brief Main program file for the student-course program.
 */

/**
 * \brief Main function for the student-course program.
 *
 * This function initializes the MATH101 course, enrolls random students, and
 * prints course information, the top student, and the passing students.
 *
 * @return Exit status. 0 if the program executes successfully.
 * @note The random number generator is seeded with the current time to ensure unique results.
 * @attention Make sure to include the necessary header files and properly initialize the course structure.
 * @warning Incorrectly initialized course data may lead to incorrect output or runtime errors.
 */
int main()
{
  srand((unsigned) time(NULL));

  Course *MATH101 = calloc(1, sizeof(Course));
  strcpy(MATH101->name, "Basics of Mathematics");
  strcpy(MATH101->code, "MATH 101");

  for (int i = 0; i < 20; i++) 
    enroll_student(MATH101, generate_random_student(8));
  
  print_course(MATH101);

  Student *student;
  student = top_student(MATH101);
  printf("\n\nTop student: \n\n");
  print_student(student);

  int total_passing;
  Student *passing_students = passing(MATH101, &total_passing);
  printf("\nTotal passing: %d\n", total_passing);
  printf("\nPassing students:\n\n");
  for (int i = 0; i < total_passing; i++) print_student(&passing_students[i]);
  
  return 0;
}

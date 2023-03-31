#include "student.h"
#include <stdbool.h>
/**
 * @file course.h
 * @author Ankur Pandey
 * @date 2023-03-30
 * @brief Header file for the Course struct and associated functions.
 */
  
/**
 * @brief Course information struct
 *
 * This struct contains information about a course, including the course name,
 * course code, an array of enrolled students, and the total number of enrolled
 * students.
 */
typedef struct _course {
    char name[100]; /**< Course name */
    char code[10]; /**< Course code */
    Student *students; /**< Array of enrolled students */
    int total_students; /**< Total number of enrolled students */
} Course;

/**
 * \brief Enrolls a student in a course.
 *
 * This function takes a course and a student as input, and enrolls the student
 * in the specified course.
 *
 * @param course Pointer to the course in which the student will be enrolled.
 * @param student Pointer to the student to be enrolled.
 * @note Assumes the course's student array has enough space to store the new student.
 * @attention Make sure the student is not already enrolled in the course.
 * @warning Failing to validate the student's enrollment may lead to duplicate records.
 */
void enroll_student(Course *course, Student *student);

/**
 * \brief Prints a course's information.
 *
 * This function takes a course as input and prints the course's information, including
 * the enrolled students.
 *
 * @param course Pointer to the course whose information will be printed.
 * @note Useful for debugging and displaying course data.
 * @attention Make sure the course data is properly initialized before calling this function.
 * @warning Incorrectly initialized course data may lead to incorrect output or runtime errors.
 */
void print_course(Course *course);

/**
 * \brief Finds the top student in a course.
 *
 * This function takes a course as input and returns the student with the highest average
 * grade in the course.
 *
 * @param course Pointer to the course for which the top student will be found.
 * @return Pointer to the top student in the course.
 * @note Assumes the course has at least one student enrolled.
 * @attention Verify that the course's student array is not empty.
 * @warning Failing to validate the student array may lead to incorrect results or runtime errors.
 */
Student *top_student(Course* course);

/**
 * \brief Finds the students who are passing the course.
 *
 * This function takes a course as input and returns an array of students who are
 * passing the course (with an average grade >= 50) and updates the total_passing variable.
 *
 * @param course Pointer to the course for which passing students will be found.
 * @param total_passing Pointer to an integer that will store the total number of passing students.
 * @return Pointer to an array of passing students.
 * @note Assumes the course has at least one student enrolled.
 * @attention Verify that the course's student array is not empty.
 * @warning Failing to validate the student array may lead to incorrect results or runtime errors.
 */
Student *passing(Course* course, int *total_passing);

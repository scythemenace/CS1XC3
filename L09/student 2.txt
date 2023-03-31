/**
 * @file student.h
 * @author Ankur Pandey
 * @date 2023-03-30
 * @brief Header file for the Student struct and associated functions.
 */ 
/**
 * @brief Student information struct
 *
 * This struct contains information about a student, including their first name,
 * last name, student ID, an array of grades, and the number of grades in the
 * array.
 */
typedef struct _student {
    char first_name[50]; /**< Student's first name */
    char last_name[50]; /**< Student's last name */
    char id[11]; /**< Student ID */
    double *grades; /**< Array of grades */
    int num_grades; /**< Number of grades in the array */
} Student;

/**
 * \brief Adds a grade to a student's grade array.
 *
 * This function takes a student and a grade as input and adds the grade to
 * the student's array of grades.
 *
 * @param student Pointer to the student whose grade will be added.
 * @param grade The grade to be added.
 * @note Assumes the student's grade array has enough space to store the new grade.
 * @attention Make sure the grade is a valid value between 0 and 100.
 * @warning Failing to validate the grade value may lead to incorrect results.
 */
void add_grade(Student *student, double grade);

/**
 * \brief Calculates the average of a student's grades.
 *
 * This function takes a student as input and calculates the average of the student's grades.
 *
 * @param student Pointer to the student whose grades will be averaged.
 * @return The average of the student's grades.
 * @note Assumes the student has at least one grade in the array.
 * @attention Verify that the student's grade array is not empty.
 * @warning Failing to validate the grade array may lead to incorrect results or runtime errors.
 */
double average(Student *student);

/**
 * \brief Prints a student's information.
 *
 * This function takes a student as input and prints the student's information.
 *
 * @param student Pointer to the student whose information will be printed.
 * @note Useful for debugging and displaying student data.
 * @attention Make sure the student data is properly initialized before calling this function.
 * @warning Incorrectly initialized student data may lead to incorrect output or runtime errors.
 */
void print_student(Student *student);

/**
 * \brief Generates a random student with a specified number of grades.
 *
 * This function generates a random student with the given number of grades.
 *
 * @param grades The number of grades for the random student.
 * @return Pointer to the generated random student.
 * @note The random student's name, ID, and grades are randomly generated.
 * @attention Ensure that the random number generator is properly seeded to avoid repeated results.
 * @warning The returned student pointer should be deal with by the caller.
 */
Student* generate_random_student(int grades);




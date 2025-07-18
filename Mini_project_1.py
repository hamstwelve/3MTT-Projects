{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1dd047c5",
   "metadata": {
    "id": "1dd047c5"
   },
   "source": [
    "\n",
    "# Mini Project - Week 1\n",
    "\n",
    "© Darey.io"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69fb6aa8",
   "metadata": {
    "id": "69fb6aa8"
   },
   "source": [
    "### This project covers:\n",
    "\n",
    "1. Python Data Structures\n",
    "2. Loops\n",
    "3. If Statements\n",
    "4. List Comprehension\n",
    "5. Lambda Functions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "641d6406",
   "metadata": {
    "id": "641d6406"
   },
   "source": [
    "### Number of Questions: 8\n",
    "\n",
    "#### Instructions:\n",
    "\n",
    "You are provided with a set of 8 questions designed to help you practice and apply your knowledge of Python data structures, loops, if statements, list comprehensions, and lambda functions. Each question includes the beginning part of the code and the expected output. Your task is to complete the missing parts of the code to achieve the expected output."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c13127b3",
   "metadata": {
    "id": "c13127b3"
   },
   "source": [
    "### Question 1: Filter Even Numbers\n",
    "#### Objective: Use list comprehension and if statement to filter even numbers from a given list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7b9219d5",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "7b9219d5",
    "outputId": "385e06bc-556b-45e1-d633-b41c8d8958e4"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "# Given list of numbers\n",
    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "# Your task: Use list comprehension to create a new list 'even_numbers' that contains only the even numbers from 'numbers'\n",
    "\n",
    "# Write your code below\n",
    "even_numbers = [num for num in numbers if num % 2 == 0]\n",
    "print(even_numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c67dca7b",
   "metadata": {
    "id": "c67dca7b"
   },
   "source": [
    "```Python\n",
    "Expected Output: [2, 4, 6, 8, 10]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "deb47b2a",
   "metadata": {
    "id": "deb47b2a"
   },
   "source": [
    "### Question 2: Square Numbers Using Lambda\n",
    "#### Objective: Use a lambda function function to square each number in a given list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9b63f47d",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "9b63f47d",
    "outputId": "8f6dbc49-2f0c-435a-ec96-a04a40c7068e"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25]\n"
     ]
    }
   ],
   "source": [
    "# Given list of numbers\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "# Your task: Use a lambda function to create a new list 'squared_numbers' where each element is the\n",
    "# square of the corresponding element in 'numbers'\n",
    "\n",
    "# Write your code below\n",
    "squared_numbers = list(map(lambda x: x**2, numbers))\n",
    "print(squared_numbers)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e60a7fa2",
   "metadata": {
    "id": "e60a7fa2"
   },
   "source": [
    "```Python\n",
    "Expected Output: [1, 4, 9, 16, 25]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9b7ee55",
   "metadata": {
    "id": "b9b7ee55"
   },
   "source": [
    "### Question 3: Nested Loop for Matrix Transposition\n",
    "\n",
    "#### Objective: Use nested loops to transpose a given matrix."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "37a40c77",
   "metadata": {
    "id": "37a40c77",
    "outputId": "e629498e-5053-4dac-f9c3-7913b61edb7b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 7]\n",
      "[2, 5, 8]\n",
      "[3, 6, 9]\n"
     ]
    }
   ],
   "source": [
    "# Given matrix\n",
    "matrix = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "# Your task: Use nested loops to create a new matrix 'transposed_matrix' which is the transpose of 'matrix'\n",
    "\n",
    "# Initialize the transposed matrix with the correct dimensions\n",
    "# Write your code below\n",
    "transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]\n",
    "for t in transposed_matrix:\n",
    "    print(t)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c66deff",
   "metadata": {
    "id": "9c66deff"
   },
   "source": [
    "```Python\n",
    "Expected Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "244251b8",
   "metadata": {
    "id": "244251b8"
   },
   "source": [
    "### Question 4: Flatten a Nested List\n",
    "\n",
    "#### Objective: Use nested loops and list comprehension to flatten a nested list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7ee66b2e",
   "metadata": {
    "id": "7ee66b2e",
    "outputId": "8baa47f5-7063-432a-b495-af6673a3ffd7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "# Given nested list\n",
    "nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]\n",
    "\n",
    "# Your task: Use nested loops and list comprehension to create a new list 'flattened_list' that contains all the\n",
    "# elements of 'nested_list' in a single list\n",
    "\n",
    "# Write your code below\n",
    "flattened_list = [numbers for sublist in nested_list for numbers in sublist]\n",
    "print(flattened_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15b06c85",
   "metadata": {
    "id": "15b06c85"
   },
   "source": [
    "```Python\n",
    "Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "defd49c9",
   "metadata": {
    "id": "defd49c9"
   },
   "source": [
    "### Question 5: Dictionary from Two Lists\n",
    "\n",
    "#### Objective: Use a loop and if statement to create a dictionary from two lists."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4fde6ecd",
   "metadata": {
    "id": "4fde6ecd",
    "outputId": "f0cc6260-e9dc-4e69-848c-1f0b9c06fed0"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Alice', 'age': 25, 'city': 'New York'}\n"
     ]
    }
   ],
   "source": [
    "# Given two lists\n",
    "keys = ['name', 'age', 'city']\n",
    "values = ['Alice', 25, 'New York']\n",
    "\n",
    "# Your task: Use a loop and if statement to create a dictionary 'my_dict' where elements from 'keys' are keys and\n",
    "# elements from 'values' are values\n",
    "my_dict = {}\n",
    "for i in range(len(keys)):\n",
    "    my_dict[keys[i]] = values[i]\n",
    "print(my_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9519c012",
   "metadata": {
    "id": "9519c012"
   },
   "source": [
    "```Python\n",
    "Expected Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5063f62e",
   "metadata": {
    "id": "5063f62e"
   },
   "source": [
    "### Question 6: Filter and Transform Dictionary\n",
    "\n",
    "#### Objective: Use a lambda function, filter, and dictionary comprehension to filter and transform a dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "01d3c444",
   "metadata": {
    "id": "01d3c444",
    "outputId": "dc0631ec-9052-4c98-fd6a-aba7433c2e63"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Alice': 90, 'Bob': 80, 'Charlie': 100}\n"
     ]
    }
   ],
   "source": [
    "# Given dictionary\n",
    "students = {\n",
    "    'Alice': 85,\n",
    "    'Bob': 75,\n",
    "    'Charlie': 95,\n",
    "    'David': 65,\n",
    "    'Eve': 50\n",
    "}\n",
    "\n",
    "# Your task: Use a lambda function, filter, and dictionary comprehension to create a new dictionary 'passed_students'\n",
    "# with students who scored more than 70. Add 5 bonus points to their scores.\n",
    "\n",
    "# Write your code below\n",
    "def students_bonus_addition(students):\n",
    "    passed_students = {name: score + 5 for name, score in filter(lambda item: item[1] > 70, students.items())}\n",
    "    return passed_students\n",
    "new_students_score = students_bonus_addition(students)\n",
    "print(new_students_score)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47161247",
   "metadata": {
    "id": "47161247"
   },
   "source": [
    "```Python\n",
    "Expected Output: {'Alice': 90, 'Bob': 80, 'Charlie': 100}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a126fbc",
   "metadata": {
    "id": "9a126fbc"
   },
   "source": [
    "### Question 7: Grouping Elements by Parity\n",
    "\n",
    "#### Objective: Use a loop, if statement, and list comprehension to group elements of a list by parity (even or odd)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2d63db15",
   "metadata": {
    "id": "2d63db15",
    "outputId": "1d024b3a-46d8-43d0-cf9b-a073829ff72c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'even': [2, 4, 6, 8, 10], 'odd': [1, 3, 5, 7, 9]}\n"
     ]
    }
   ],
   "source": [
    "# Given list of numbers\n",
    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "# Your task: Use a loop, if statement, and list comprehension to create a dictionary 'grouped_numbers' with two\n",
    "# keys: 'even' and 'odd', containing even and odd numbers respectively.\n",
    "\n",
    "# Write your code below\n",
    "grouped_numbers = {\n",
    "    'even': [numbers for numbers in numbers if numbers % 2 == 0],\n",
    "    'odd': [numbers for numbers in numbers if numbers % 2 != 0]\n",
    "}\n",
    "print(grouped_numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "375f2559",
   "metadata": {
    "id": "375f2559"
   },
   "source": [
    "\n",
    "\n",
    "Expected Output: {'even': [2, 4, 6, 8, 10], 'odd': [1, 3, 5, 7, 9]}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73e9f049",
   "metadata": {
    "id": "73e9f049"
   },
   "source": [
    "### Question 8: Fibonacci Sequence Generator\n",
    "\n",
    "#### Objective: Use a loop and if statement to generate the first n Fibonacci numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "cb525a00",
   "metadata": {
    "id": "cb525a00",
    "outputId": "22c88264-6acd-4aaa-d974-ffa1766a7e08"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
     ]
    }
   ],
   "source": [
    "# Given a number n\n",
    "n = 10\n",
    "\n",
    "# Your task: Use a loop and if statement to create a list 'fibonacci' containing the first n Fibonacci numbers\n",
    "\n",
    "# Write your code below\n",
    "\n",
    "fibonacci = [0, 1]\n",
    "n = 10\n",
    "\n",
    "# Use a loop to generate the remaining Fibonacci numbers\n",
    "for i in range(2, n):\n",
    "    fibonacci.append(fibonacci[-1] + fibonacci[-2])\n",
    "print(fibonacci)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae542aa8",
   "metadata": {
    "id": "ae542aa8"
   },
   "source": [
    "```Python\n",
    "Expected Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import pandas as pd
import string
import re  

# Load the course data
data = pd.read_csv('/Users/shaunaksachdev/Desktop/courses.csv')


data['course code'] = data['course code'].str.upper().str.strip()


def chatbot():
    while True:
        query = input("Ask a question about courses (or type 'exit' to quit): ").lower()
        if query == 'exit':
            print("Goodbye!")
            break

        # Using regex to extract the course code from the query
        match = re.search(r'[A-Z]{3,4} \d{3,4}', query.upper())  # Regex to find course codes 
        if match:
            course = match.group(0)
            print(f"Searching for course: {course}")  # Debugging 
        else:
            print("No course code found in your query.")
            continue

        if "prerequisite" in query:
            result = data[data['course code'] == course]
            if not result.empty:
                prereq = result['prerequisites'].values[0]
                print(f"The prerequisite for {course} is: {prereq if prereq else 'None'}")
            else:
                print(f"Course {course} not found.")

        elif "alternative" in query:
            result = data[data['course code'] == course]
            if not result.empty:
                alt = result['alternatives'].values[0]
                print(f"The alternative for {course} is: {alt if alt else 'None'}")
            else:
                print(f"Course {course} not found.")

        elif "credit" in query or "credits" in query:
            result = data[data['course code'] == course]
            if not result.empty:
                credits = result['credits'].values[0]
                print(f"The course {course} offers {credits} credits.")
            else:
                print(f"Course {course} not found.")

        elif "title" in query or "description" in query:
            result = data[data['course code'] == course]
            if not result.empty:
                title = result['title'].values[0]
                print(f"The title of {course} is: {title}")
            else:
                print(f"Course {course} not found.")

        elif "list all" in query or "available courses" in query:
            courses = data['course code'].tolist()
            print(f"Available courses: {', '.join(courses)}")

        elif "details" in query:
            result = data[data['course code'] == course]
            if not result.empty:
                details = result.iloc[0].to_dict()
                details_string = ', '.join([f"{key}: {value}" for key, value in details.items()])
                print(f"Details for {course}: {details_string}")
            else:
                print(f"Course {course} not found.")

        elif "courses with" in query and "credits" in query:
            try:
                credits = int(query.split("with")[-1].strip().split()[0])
                result = data[data['credits'] == credits]
                courses = result['course code'].tolist()
                if courses:
                    print(f"Courses offering {credits} credits: {', '.join(courses)}")
                else:
                    print(f"No courses found offering {credits} credits.")
            except ValueError:
                print("Please specify a valid number of credits.")

        else:
            print("I'm sorry, I can only answer questions about prerequisites, alternatives, credits, titles, details, or available courses.")

print("Available course codes in dataset:", data['course code'].unique())

chatbot()
#!/usr/bin/env python
# coding: utf-8

# # a).

# ## Load Data from CSV into a List:

# In[1]:


import csv

def load_csv_to_list(file_path):
    data_list = []
    headers = []
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)  # Read the header row
            if headers is None:
                print("Warning: The file is empty or does not have a header row.")
            for row in csv_reader:
                data_list.append(row)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: An I/O error occurred.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return data_list, headers


def print_com728():
    print("COM728")
    print("COM728")
    print("COM728")


# In[3]:


file_path = input("Please enter the path to the CSV file: ")
data, headers = load_csv_to_list(file_path)


# ## Task a1: Retrieve specific columns based on ID

# In[4]:


def retrieve_by_id(data, headers, student_id):
    print_com728()
    try:
        id_index = headers.index("ID")
        sex_index = headers.index("Sex")
        age_index = headers.index("Age")
        family_relative_index = headers.index("Family_relative")
        state_index = headers.index("State")
        race_index = headers.index("Race")
        
        result = [row for row in data if row[id_index] == student_id]
        if result:
            for row in result:
                print(f"Sex: {row[sex_index]}, Age: {row[age_index]}, "
                      f"Number of Relatives: {row[family_relative_index]}, "
                      f"State: {row[state_index]}, Race: {row[race_index]}")
        else:
            print(f"No data found for ID: {student_id}")
    except ValueError:
        print("Error: One or more columns are missing in the dataset.")

# Retrieve information based on a specific ID        
retrieve_by_id(data, headers, "ID-371")


# ## Task a2: Retrieve specific columns based on race

# In[5]:


def retrieve_by_race(data, headers, specific_race):
    print_com728()
    try:
        race_index = headers.index("Race")
        sex_index = headers.index("Sex")
        school_support_index = headers.index("School_support")
        access_internet_index = headers.index("Access_internet")
        attendance_rate_index = headers.index("Attendance_rate")
        parental_involvement_index = headers.index("Parental_involvement")
        
        result = [row for row in data if row[race_index] == specific_race]
        for row in result:
            print(f"Sex: {row[sex_index]}, School Support: {row[school_support_index]}, "
                  f"Access Internet: {row[access_internet_index]}, "
                  f"Attendance Rate: {row[attendance_rate_index]}, "
                  f"Parental Involvement: {row[parental_involvement_index]}")
    except ValueError:
        print("Error: One or more columns are missing in the dataset.")

# Retrieve information based on a specific race
retrieve_by_race(data, headers, "Asian")


# ## Task a3: Retrieve specific columns based on absences and parental involvement

# In[6]:


def retrieve_by_absences(data, headers, max_absences, parental_involvement):
    print_com728()
    try:
        id_index = headers.index("ID")
        free_time_index = headers.index("Freetime")
        math_score_index = headers.index("Math_score")
        reading_score_index = headers.index("Reading_score")
        writing_score_index = headers.index("Writing_score")
        absences_index = headers.index("Absences")
        parental_involvement_index = headers.index("Parental_involvement")
        
        result = [row for row in data if int(row[absences_index]) < max_absences and row[parental_involvement_index] == parental_involvement]
        for row in result:
            print(f"ID: {row[id_index]}, Free Time: {row[free_time_index]}, "
                  f"Math Score: {row[math_score_index]}, Reading Score: {row[reading_score_index]}, "
                  f"Writing Score: {row[writing_score_index]}")
    except ValueError:
        print("Error: One or more columns are missing in the dataset.")

# Retrieve information based on absences and parental involvement
retrieve_by_absences(data, headers, 50, "low")


# ## Task a4: Retrieve specific columns with a new condition

# In[7]:


def retrieve_specific_condition(data, headers):
    print_com728()
    try:
        sex_index = headers.index("Sex")
        studytime_index = headers.index("Studytime")
        health_index = headers.index("Health")
        
        # condition: Retrieve students who study more than 2 hours per week and have good health
        result = [row for row in data if int(row[studytime_index]) > 2 and row[health_index] == "good"]
        for row in result:
            print(f"Sex: {row[sex_index]}, Study Time: {row[studytime_index]}, Health: {row[health_index]}")
    except ValueError:
        print("Error: One or more columns are missing in the dataset.")

# Retrieve information based on a specific condition
retrieve_specific_condition(data, headers)


# # b).

# In[8]:


import pandas as pd

def load_csv_to_dataframe(file_path):
    try:
        # Load CSV data into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def print_com728():
    print("COM728")
    print("COM728")
    print("COM728")


# In[9]:


# Load the data into a DataFrame
file_path = "Downloads/students_data.csv"  # Replace with the path to your CSV file
df = load_csv_to_dataframe(file_path)
df


# ## Task b1: Top 3 Levels of Mother’s Education for a Specific Race

# In[10]:


def top_3_mother_education_by_race(df, specific_race):
    print_com728()
    try:
        # Filter data by the specific race
        filtered_df = df[df['Race'] == specific_race]
        
        # Group by mother's education level and count the occurrences
        education_counts = filtered_df['Mother_education_level '].value_counts()
        
        # Get top 3 levels
        top_3_education = education_counts.head(3)
        
        print(f"Top 3 levels of mother's education for race '{specific_race}':")
        print(top_3_education)
    except KeyError as e:
        print(f"Error: Column not found - {e}")
        
top_3_mother_education_by_race(df, "Asian")  # Replace with the specific race


# ## Task b2: Average Number of Absences for a Specific Parental Involvement Level

# In[11]:


def avg_absences_by_parental_involvement(df, parental_involvement_level):
    print_com728()
    try:
        # Filter data by parental involvement level
        filtered_df = df[df['Parental_involvement'] == parental_involvement_level]
        
        # Calculate average number of absences
        avg_absences = filtered_df['Absences'].mean()
        
        print(f"Average number of absences for parental involvement level '{parental_involvement_level}':")
        print(avg_absences)
    except KeyError as e:
        print(f"Error: Column not found - {e}")
        
avg_absences_by_parental_involvement(df, "low")  # Replace with the specific level of parental involvement


# ## Task b3: Average Math Score for Students with Attendance Rate Greater Than 80%, Based on Race

# In[12]:


def avg_math_score_by_attendance_rate_and_race(df, min_attendance_rate):
    print_com728()
    try:
        # Filter data by attendance rate
        filtered_df = df[df['Attendance_rate'] > min_attendance_rate]
        
        # Group by race and calculate average math score
        avg_math_scores = filtered_df.groupby('Race')['Math_score'].mean()
        
        print(f"Average math score for students with attendance rate greater than {min_attendance_rate}%:")
        print(avg_math_scores)
    except KeyError as e:
        print(f"Error: Column not found - {e}")

avg_math_score_by_attendance_rate_and_race(df, 80)  # Attendance rate threshold is 80%


# ## Task b4: Custom Analysis Based on Unique Selection and Condition

# In[13]:


def custom_analysis(df):
    print_com728()
    try:
        # Example: Analyze the average writing score for students who participate in extracurricular activities
        filtered_df = df[df['Activities'] == 'yes']
        
        # Calculate average writing score
        avg_writing_score = filtered_df['Writing_score'].mean()
        
        print(f"Average writing score for students who participate in extracurricular activities:")
        print(avg_writing_score)
    except KeyError as e:
        print(f"Error: Column not found - {e}")


custom_analysis(df)


# # c).

# ## Task c1: Proportion of Students Based on Race

# In[14]:


import matplotlib.pyplot as plt

def plot_race_proportions(df):
    print_com728()
    try:
        # Count occurrences of each race
        race_counts = df['Race'].value_counts()
        
        # Plot pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Proportion of Students Based on Race')
        plt.show()
    except KeyError as e:
        print(f"Error: Column not found - {e}")

plot_race_proportions(df)


# ## Task c2: Average Writing Scores Among Students in Each Race Group

# In[15]:


def plot_avg_writing_scores_by_race(df):
    print_com728()
    try:
        # Calculate average writing scores for each race
        avg_writing_scores = df.groupby('Race')['Writing_score'].mean()
        
        # Plot bar chart
        plt.figure(figsize=(10, 6))
        avg_writing_scores.plot(kind='bar', color='skyblue')
        plt.xlabel('Race')
        plt.ylabel('Average Writing Score')
        plt.title('Average Writing Scores by Race')
        plt.xticks(rotation=45)
        plt.show()
    except KeyError as e:
        print(f"Error: Column not found - {e}")

plot_avg_writing_scores_by_race(df)


# ## Task c3: Relationship Between Reading and Writing Scores

# In[16]:


def plot_reading_vs_writing_scores(df):
    print_com728()
    try:
        # Plot scatter plot
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Reading_score'], df['Writing_score'], alpha=0.5, color='green')
        plt.xlabel('Reading Score')
        plt.ylabel('Writing Score')
        plt.title('Relationship Between Reading and Writing Scores')
        plt.grid(True)
        plt.show()
    except KeyError as e:
        print(f"Error: Column not found - {e}")

plot_reading_vs_writing_scores(df)


# ## Task c4: Custom Visualization of Student Performance

# In[17]:


def plot_absences_vs_math_scores(df):
    print_com728()
    try:
        # Plot scatter plot
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Absences'], df['Math_score'], alpha=0.5, color='purple')
        plt.xlabel('Absences')
        plt.ylabel('Math Score')
        plt.title('Relationship Between Absences and Math Scores')
        plt.grid(True)
        plt.show()
    except KeyError as e:
        print(f"Error: Column not found - {e}")

plot_absences_vs_math_scores(df)


# In[5]:


import pandas as pd
pd.set_option("display.max.columns", None)

# Load the data into a DataFrame
df = pd.read_csv("Downloads/students_data.csv")  # Replace with the path to your CSV file
df


# In[ ]:





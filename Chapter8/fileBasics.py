#File Handling ---
#python program allows that handles file like store ,read ,write and manage data
#which is saved on computer ,such as notes, log , student records ,CSV files



# ==============================================================================
#                      FILE HANDLING IN PYTHON: A COMPLETE GUIDE
# ==============================================================================
# Think of file handling in Python like working with a physical book.
# To read or write, you must:
#   1. Open the book (Open the file)
#   2. Read the pages or write a new note (Read / Write data)
#   3. Close the book (Close the file to save memory and protect it from damage)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE TRADITIONAL WAY (Open, Do something, Close)
# ------------------------------------------------------------------------------
# This is how file handling works fundamentally. You open it, do your work,
# and explicitly close it.

# Step 1: Open the file
# 'w' means Write mode. If the file doesn't exist, Python creates it.
# WARNING: 'w' wipes out any text already in that file!
file = open("example.txt", "w")

# Step 2: Write some text into it
file.write("Hello, Python!\n")
file.write("This is a traditional way to write files.\n")

# Step 3: Crucial! Close the file.
# If you forget this, the data might not save, and the file stays locked in memory.
file.close()


# ------------------------------------------------------------------------------
# 2. THE MODERN & BETTER WAY: Using "with" (The Context Manager)
# ------------------------------------------------------------------------------
# In the real world, Python programmers rarely use .close(). Instead, we use
# the 'with' statement. It automatically closes the file for you, even if your
# code crashes halfway through!

# Writing using 'with'
with open("cool_story.txt", "w") as story_file:
    story_file.write("Once upon a time, a programmer forgot to close a file...\n")
    story_file.write("But then they learned about the 'with' keyword!\n")
# Look ma, no .close() needed! It closed the second we un-indented.


# ------------------------------------------------------------------------------
# 3. READING FROM A FILE
# ------------------------------------------------------------------------------
# To read a file, we change the mode to 'r' (Read mode).

# Method A: Reading the entire file at once as one big string
with open("cool_story.txt", "r") as story_file:
    content = story_file.read()
    print("--- Reading Entire File ---")
    print(content)

# Method B: Reading line-by-line (Best for massive files so you don't run out of RAM)
with open("cool_story.txt", "r") as story_file:
    print("--- Reading Line by Line ---")
    for line in story_file:
        # we use .strip() to remove extra hidden newline (\n) gaps
        print(line.strip())


    # ------------------------------------------------------------------------------
# 4. APPENDING TO A FILE (Adding text without deleting what's already there)
# ------------------------------------------------------------------------------
# If you use 'w', Python destroys the old file and starts fresh.
# If you want to *add* to the end of a file, use 'a' (Append mode).

with open("cool_story.txt", "a") as story_file:
    story_file.write("And they lived happily ever after.\n")


# ------------------------------------------------------------------------------
# QUICK CHEAT SHEET: FILE MODES
# ------------------------------------------------------------------------------
# 'r'  -> Read mode (Default). Fails if the file does not exist.
# 'w'  -> Write mode. Overwrites existing file or creates a new one.
# 'a'  -> Append mode. Adds text to the end of the file. Creates it if missing.
# 'r+' -> Read AND Write mode.
# 'rb' or 'wb' -> Read/Write in Binary mode (Used for images, videos, audio, PDFs).
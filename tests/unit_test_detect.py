import os, cv2

# Get the current working directory
current_dir = os.getcwd()

# Get the parent directory
parent_directory = os.path.dirname(current_dir)

subdirectory = 'static'

# Get the app directory
directory = os.path.join(parent_directory, subdirectory)

# Print the parent directory
print(directory)

# Get the list of files and directories within the specified directory
contents = os.listdir(directory)

# Print the names of files and directories
for item in contents:
    print(item)

img = cv2.imread(os.path.join(parent_directory, subdirectory, 'agilim.png'))
cv2.imshow("image", img) 
cv2.waitKey()
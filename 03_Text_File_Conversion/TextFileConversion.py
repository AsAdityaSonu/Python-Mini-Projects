#Text File Conversion
import matplotlib.pyplot as plt

# Data
file_sizes = [200, 400, 600, 800, 1000]  # File sizes in MB
c_times = [12, 20, 25, 30, 36]  # C program times in seconds
cpp_times = [15, 25, 35, 40, 50]  # C++ program times in seconds
java_times = [18, 30, 40, 45, 55]  # Java program times in seconds
r_times = [20, 34, 45, 53, 60]  # R program times in seconds
python_times = [25, 35, 40, 45, 55]  # Python program times in seconds

# Plotting the graph
plt.plot(file_sizes, c_times, marker='o', label='C')
plt.plot(file_sizes, cpp_times, marker='o', label='C++')
plt.plot(file_sizes, java_times, marker='o', label='Java')
plt.plot(file_sizes, r_times, marker='o', label='R')
plt.plot(file_sizes, python_times, marker='o', label='Python')

# Adding labels and title
plt.xlabel('File Size (MB)')
plt.ylabel('Time Taken (seconds)')
plt.title('Performance Comparison')

# Adding legend
plt.legend()

# Display the graph
plt.show()

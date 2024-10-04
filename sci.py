import matplotlib.pyplot as plt
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time

# Define a handler that will trigger updates on file change
class CSVUpdateHandler(FileSystemEventHandler):
    def __init__(self, file_path, update_func):
        self.file_path = file_path
        self.update_func = update_func

    def on_modified(self, event):
        if event.src_path.endswith(self.file_path):
            print(f"{self.file_path} has been modified.")
            self.update_func()  # Call the update function when file changes

# Function to reload the CSV and update the plot
def update_plot():
    # Load the CSV file
    df = pd.read_csv('Guess.csv')

    # Clean column names (remove leading/trailing spaces)
    df.columns = df.columns.str.strip()

    # Check if necessary columns exist
    if 'Number of tries' in df.columns and 'Wins' in df.columns and 'Losses' in df.columns:
        # Clear the previous plot
        plt.clf()

        # Plot the data
        plt.plot(df['Number of tries'], df['Wins'], label='Wins', marker='o')
        plt.plot(df['Number of tries'], df['Losses'], label='Losses', marker='x')
        plt.title('Wins and Losses Over Number of Tries')
        plt.xlabel('Number of Tries')
        plt.ylabel('Wins / Losses')
        plt.legend()
        plt.grid(True)

        # Redraw the plot and refresh the window
        plt.draw()
        plt.pause(0.1)  # Pause to allow Matplotlib to refresh
    else:
        print("Error: Required columns are missing in the CSV.")

# Set up real-time file monitoring
def monitor_csv(file_path):
    # Create an event handler for the CSV file
    event_handler = CSVUpdateHandler(file_path, update_plot)

    # Create an observer to watch the file
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)

    # Start the observer in the background
    observer.start()
    return observer

# Run the Matplotlib GUI in the main thread
def run_gui():
    plt.ion()  # Interactive mode on for real-time updates
    update_plot()  # Initial plot
    plt.show()

    while True:
        plt.pause(1)  # Keep plot responsive in the main thread

# Run the observer in a separate thread
def run_monitor():
    observer = monitor_csv('Guess.csv')
    return observer

# Start the observer and plot in the correct threads
if __name__ == "__main__":
    observer = run_monitor()  # Start file observer in the background

    try:
        run_gui()  # Run GUI (Matplotlib) in the main thread
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

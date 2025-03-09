import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

class PythonTestGUI:
    # Initialize the GUI with a title and window size. Initialize variables to store file paths.
    def __init__(self, root):
        self.root = root
        self.root.title("Python Test GUI")
        self.root.geometry("400x300")  # Set a reasonable window size

        self.code_file = None
        self.output_file = None

        # File selection
        self.file_label = tk.Label(root, text="No code file selected")
        self.file_label.pack(pady=10)

        self.select_file_button = tk.Button(root, text="Select Code File", command=self.select_code_file)
        self.select_file_button.pack(pady=10)

        self.execute_test_button = tk.Button(root, text="Execute Test", command=self.show_test_menu, state=tk.DISABLED)
        self.execute_test_button.pack(pady=10)

    def select_code_file(self):
        """Select a code file to simulate flashing."""
        self.code_file = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if self.code_file:
            self.file_label.config(text=f"Selected: {os.path.basename(self.code_file)}")
            self.execute_test_button.config(state=tk.NORMAL)

    def show_test_menu(self):
        """Display a menu for test execution."""
        if not self.code_file:
            messagebox.showerror("Error", "Please select a code file first!")
            return

        test_window = tk.Toplevel(self.root)
        test_window.title("Test Execution Menu")
        test_window.geometry("300x200")

        tk.Label(test_window, text="Choose a test option:").pack(pady=10)

        successful_execution_button = tk.Button(
            test_window, text="Successful Execution", command=lambda: self.run_test("success")
        )
        successful_execution_button.pack(pady=5)

        choose_test_output_button = tk.Button(
            test_window, text="Choose Test Output", command=self.select_output_file
        )
        choose_test_output_button.pack(pady=5)

    def select_output_file(self):
        """Select the desired output file and run the comparison test."""
        self.output_file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if self.output_file:
            self.run_test("compare")

    def run_test(self, test_type):
        """Execute the selected test."""
        if not self.code_file:
            messagebox.showerror("Error", "No code file selected!")
            return

        command = ["./main"]
        if test_type == "success":
            command += ["--success", f'"{self.code_file}"']
        elif test_type == "compare" and self.output_file:
            command += ["--compare", f'"{self.code_file}"', f'"{self.output_file}"']

        print("Executing command:", " ".join(command))  # Log the command

        try:
            process = subprocess.run(
                " ".join(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, cwd=os.getcwd()
            )

            if process.returncode == 0:
                messagebox.showinfo("Test Result", process.stdout.strip())
            else:
                messagebox.showerror("Test Error", process.stderr.strip() or process.stdout.strip())
        except FileNotFoundError:
            messagebox.showerror("Error", "The main executable was not found. Ensure it is in the current directory.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute the test: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonTestGUI(root)
    root.mainloop()
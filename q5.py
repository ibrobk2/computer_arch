import tkinter as tk
from tkinter import ttk

class PipelineSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Instruction Pipelining Simulator")
        self.instructions = []

        self.pipeline_stages = ["Fetch", "Decode", "Execute", "Memory Access", "Write Back"]
        self.pipeline_data = [tk.StringVar() for _ in range(len(self.pipeline_stages))]

        self.create_widgets()

    def create_widgets(self):
        instruction_label = ttk.Label(self.root, text="Enter Instructions:")
        instruction_label.grid(row=0, column=0, padx=5, pady=5)

        self.instruction_entry = ttk.Entry(self.root, width=40)
        self.instruction_entry.grid(row=0, column=1, padx=5, pady=5)

        self.run_button = ttk.Button(self.root, text="Run", command=self.run_pipeline)
        self.run_button.grid(row=0, column=2, padx=5, pady=5)

        self.output_label = ttk.Label(self.root, text="Pipeline Status:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)

        for i, stage in enumerate(self.pipeline_stages):
            ttk.Label(self.root, text=stage).grid(row=1, column=i+1, padx=5, pady=5)
            ttk.Label(self.root, textvariable=self.pipeline_data[i]).grid(row=2, column=i+1, padx=5, pady=5)

    def run_pipeline(self):
        instructions = self.instruction_entry.get().split()
        if not instructions:
            return

        self.instructions = instructions
        self.update_pipeline()

    def update_pipeline(self):
        for i, stage in enumerate(self.pipeline_stages):
            if i < len(self.instructions):
                self.pipeline_data[i].set(self.instructions[i])
            else:
                self.pipeline_data[i].set("")

if __name__ == "__main__":
    root = tk.Tk()
    simulator = PipelineSimulator(root)
    root.mainloop()

"""
Lesson 8.2: Using External Packages - Rich

This lesson demonstrates using the rich package for enhanced terminal output,
including colors, tables, progress bars, and more.
"""

from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel
from rich.prompt import Prompt
import time
from typing import List, Dict

class EnhancedTaskManager:
    """Task manager with rich output formatting"""
    
    def __init__(self):
        self.console = Console()
        self.tasks: List[Dict[str, str]] = []
    
    def display_menu(self) -> None:
        """Display the main menu with rich formatting"""
        self.console.print(Panel.fit(
            "[bold blue]Task Manager[/bold blue]\n"
            "1. Add task\n"
            "2. Complete task\n"
            "3. List tasks\n"
            "4. Exit",
            title="Menu",
            border_style="green"
        ))
    
    def add_task(self, description: str) -> None:
        """Add a new task with progress animation"""
        for _ in track(range(3), description="Adding task..."):
            time.sleep(0.2)
        
        self.tasks.append({
            "description": description,
            "status": "Pending"
        })
        self.console.print(f"[green]✓[/green] Added task: {description}")
    
    def complete_task(self, index: int) -> None:
        """Mark a task as completed"""
        try:
            task = self.tasks[index]
            task["status"] = "Completed"
            self.console.print(f"[green]✓[/green] Completed task: {task['description']}")
        except IndexError:
            self.console.print("[red]Error:[/red] Invalid task index")
    
    def list_tasks(self) -> None:
        """Display tasks in a rich table"""
        if not self.tasks:
            self.console.print("[yellow]No tasks found[/yellow]")
            return
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Index", style="dim")
        table.add_column("Description")
        table.add_column("Status")
        
        for i, task in enumerate(self.tasks):
            status_color = "green" if task["status"] == "Completed" else "yellow"
            table.add_row(
                str(i + 1),
                task["description"],
                f"[{status_color}]{task['status']}[/{status_color}]"
            )
        
        self.console.print(table)
    
    def run(self) -> None:
        """Run the task manager"""
        while True:
            self.display_menu()
            choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"])
            
            if choice == "1":
                description = Prompt.ask("Enter task description")
                self.add_task(description)
            elif choice == "2":
                self.list_tasks()
                try:
                    index = int(Prompt.ask("Enter task number to complete")) - 1
                    self.complete_task(index)
                except ValueError:
                    self.console.print("[red]Error:[/red] Please enter a valid number")
            elif choice == "3":
                self.list_tasks()
            elif choice == "4":
                self.console.print("[blue]Goodbye![/blue]")
                break

def main():
    """Main function"""
    manager = EnhancedTaskManager()
    manager.run()

if __name__ == "__main__":
    main() 
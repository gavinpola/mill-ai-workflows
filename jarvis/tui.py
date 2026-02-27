#!/usr/bin/env python3
"""
Jarvis TUI - Agent Monitoring Dashboard for Mill AI Workflow System

A terminal-based dashboard that shows:
- Active agents and their status
- Current tasks being executed
- Execution timeline with timestamps
- Progress tracking

Usage:
    python jarvis/tui.py              # Run dashboard
    python jarvis/tui.py --demo       # Run with demo data
"""

import json
import time
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.live import Live
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID
    from rich.text import Text
    from rich.style import Style
except ImportError:
    print("Installing rich library...")
    import subprocess
    subprocess.check_call(["pip", "install", "rich"])
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.live import Live
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID
    from rich.text import Text
    from rich.style import Style

# Mill brand colors
MILL_GREEN = "green"
MILL_DARK = "dark_green"

STATE_FILE = Path(__file__).parent / "state.json"

def load_state() -> dict:
    """Load current execution state from JSON file."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return get_default_state()

def save_state(state: dict):
    """Save execution state to JSON file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2, default=str)

def get_default_state() -> dict:
    """Return default state structure."""
    return {
        "session_start": datetime.now().isoformat(),
        "current_phase": "foundation",
        "agents": [],
        "tasks": [],
        "completed_phases": [],
        "logs": []
    }

def get_demo_state() -> dict:
    """Return demo state for testing."""
    return {
        "session_start": datetime.now().isoformat(),
        "current_phase": "target_research",
        "agents": [
            {"name": "Facilitator", "status": "active", "task": "Orchestrating target research", "model": "opus"},
            {"name": "Researcher-Grocery", "status": "running", "task": "Researching Kroger, Costco, Albertsons", "model": "sonnet"},
            {"name": "Researcher-Hospitality", "status": "running", "task": "Researching Marriott, Hilton, MGM", "model": "sonnet"},
            {"name": "Researcher-FoodService", "status": "running", "task": "Researching Compass, Aramark, Sodexo", "model": "sonnet"},
            {"name": "Reviewer-Harry", "status": "idle", "task": "Waiting for outputs to review", "model": "sonnet"},
        ],
        "tasks": [
            {"name": "Directory structure", "status": "completed", "duration": "0:42"},
            {"name": "Agent prompts", "status": "completed", "duration": "3:15"},
            {"name": "WORKFLOW_WALKTHROUGH.md", "status": "completed", "duration": "1:20"},
            {"name": "Jarvis TUI", "status": "completed", "duration": "2:45"},
            {"name": "MECE scoring framework", "status": "completed", "duration": "1:30"},
            {"name": "Research wave 1", "status": "in_progress", "duration": "..."},
        ],
        "completed_phases": ["foundation"],
        "logs": [
            {"time": "00:00", "message": "Session started", "level": "info"},
            {"time": "00:42", "message": "Directory structure created", "level": "success"},
            {"time": "03:57", "message": "Agent prompts written (6 agents)", "level": "success"},
            {"time": "05:17", "message": "WORKFLOW_WALKTHROUGH.md created", "level": "success"},
            {"time": "08:02", "message": "Jarvis TUI skeleton built", "level": "success"},
            {"time": "09:32", "message": "MECE framework defined", "level": "success"},
            {"time": "09:33", "message": "Spawning parallel research agents...", "level": "info"},
            {"time": "09:34", "message": "Researcher-Grocery spawned (sonnet)", "level": "info"},
            {"time": "09:34", "message": "Researcher-Hospitality spawned (sonnet)", "level": "info"},
            {"time": "09:34", "message": "Researcher-FoodService spawned (sonnet)", "level": "info"},
        ]
    }

def create_header() -> Panel:
    """Create the header panel."""
    title = Text()
    title.append("  JARVIS  ", style="bold white on dark_green")
    title.append("  Mill AI Workflow Monitor  ", style="bold green")

    return Panel(
        title,
        style="green",
        border_style="green"
    )

def create_agents_table(agents: list) -> Table:
    """Create the agents status table."""
    table = Table(title="[bold green]Active Agents[/bold green]", border_style="green")

    table.add_column("Agent", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center")
    table.add_column("Model", style="dim")
    table.add_column("Current Task", style="white")

    status_styles = {
        "active": ("bold green", "[green]ACTIVE"),
        "running": ("bold yellow", "[yellow]RUNNING"),
        "idle": ("dim", "[dim]IDLE"),
        "completed": ("bold green", "[green]DONE"),
        "error": ("bold red", "[red]ERROR"),
    }

    for agent in agents:
        style, status_text = status_styles.get(agent["status"], ("white", agent["status"]))
        table.add_row(
            agent["name"],
            status_text,
            agent.get("model", "sonnet"),
            agent.get("task", "-")
        )

    return table

def create_tasks_table(tasks: list) -> Table:
    """Create the tasks progress table."""
    table = Table(title="[bold green]Execution Progress[/bold green]", border_style="green")

    table.add_column("Task", style="white")
    table.add_column("Status", justify="center")
    table.add_column("Duration", justify="right", style="dim")

    for task in tasks:
        if task["status"] == "completed":
            status = "[green]DONE"
        elif task["status"] == "in_progress":
            status = "[yellow]IN PROGRESS"
        else:
            status = "[dim]PENDING"

        table.add_row(task["name"], status, task.get("duration", "-"))

    return table

def create_logs_panel(logs: list, max_lines: int = 10) -> Panel:
    """Create the logs panel."""
    log_text = Text()

    for log in logs[-max_lines:]:
        time_str = log.get("time", "??:??")
        message = log.get("message", "")
        level = log.get("level", "info")

        level_styles = {
            "info": "blue",
            "success": "green",
            "warning": "yellow",
            "error": "red"
        }

        log_text.append(f"[{time_str}] ", style="dim")
        log_text.append(f"{message}\n", style=level_styles.get(level, "white"))

    return Panel(
        log_text,
        title="[bold green]Activity Log[/bold green]",
        border_style="green"
    )

def create_stats_panel(state: dict) -> Panel:
    """Create the stats panel."""
    stats = Text()

    # Session duration
    start = datetime.fromisoformat(state["session_start"])
    duration = datetime.now() - start
    minutes = int(duration.total_seconds() // 60)
    seconds = int(duration.total_seconds() % 60)

    stats.append("Session: ", style="dim")
    stats.append(f"{minutes:02d}:{seconds:02d}\n", style="bold green")

    stats.append("Phase: ", style="dim")
    stats.append(f"{state['current_phase'].replace('_', ' ').title()}\n", style="cyan")

    completed = len(state.get("completed_phases", []))
    total = 6  # Total phases
    stats.append("Progress: ", style="dim")
    stats.append(f"{completed}/{total} phases\n", style="green")

    active_agents = len([a for a in state.get("agents", []) if a["status"] in ["active", "running"]])
    stats.append("Active agents: ", style="dim")
    stats.append(f"{active_agents}\n", style="yellow")

    return Panel(
        stats,
        title="[bold green]Session Stats[/bold green]",
        border_style="green"
    )

def create_dashboard(state: dict) -> Layout:
    """Create the full dashboard layout."""
    layout = Layout()

    layout.split(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=12)
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right", ratio=2)
    )

    layout["header"].update(create_header())
    layout["left"].update(create_stats_panel(state))
    layout["right"].split(
        Layout(create_agents_table(state.get("agents", [])), name="agents"),
        Layout(create_tasks_table(state.get("tasks", [])), name="tasks")
    )
    layout["footer"].update(create_logs_panel(state.get("logs", [])))

    return layout

def run_dashboard(demo: bool = False):
    """Run the live dashboard."""
    console = Console()

    console.print("\n[bold green]Starting Jarvis...[/bold green]\n")

    if demo:
        state = get_demo_state()
        save_state(state)
    else:
        state = load_state()

    try:
        with Live(create_dashboard(state), console=console, refresh_per_second=1) as live:
            while True:
                state = load_state()
                live.update(create_dashboard(state))
                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Jarvis shutting down...[/yellow]")

# Helper functions for external updates
def add_agent(name: str, status: str = "idle", task: str = "", model: str = "sonnet"):
    """Add or update an agent in the state."""
    state = load_state()

    # Update existing or add new
    for agent in state["agents"]:
        if agent["name"] == name:
            agent["status"] = status
            agent["task"] = task
            agent["model"] = model
            save_state(state)
            return

    state["agents"].append({
        "name": name,
        "status": status,
        "task": task,
        "model": model
    })
    save_state(state)

def update_task(name: str, status: str, duration: str = ""):
    """Update a task status."""
    state = load_state()

    for task in state["tasks"]:
        if task["name"] == name:
            task["status"] = status
            if duration:
                task["duration"] = duration
            save_state(state)
            return

    state["tasks"].append({
        "name": name,
        "status": status,
        "duration": duration
    })
    save_state(state)

def add_log(message: str, level: str = "info"):
    """Add a log entry."""
    state = load_state()

    start = datetime.fromisoformat(state["session_start"])
    elapsed = datetime.now() - start
    minutes = int(elapsed.total_seconds() // 60)
    seconds = int(elapsed.total_seconds() % 60)

    state["logs"].append({
        "time": f"{minutes:02d}:{seconds:02d}",
        "message": message,
        "level": level
    })
    save_state(state)

def set_phase(phase: str):
    """Set the current phase."""
    state = load_state()
    if state["current_phase"] != phase:
        state["completed_phases"].append(state["current_phase"])
    state["current_phase"] = phase
    save_state(state)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jarvis - Mill AI Workflow Monitor")
    parser.add_argument("--demo", action="store_true", help="Run with demo data")
    args = parser.parse_args()

    run_dashboard(demo=args.demo)

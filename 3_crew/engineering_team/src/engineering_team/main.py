#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A social networking system for communities such as apartments, HOA, or a neighborhood.
The system should allow users to create an account.
The system should allow users to see posts from other users.
THe system should allow the user to like posts from others.
The system should allow users to create their own posts which is text but may include photos or videos.
The system should allow users to see announcements
The system should allow users to create accouncements which includes a subject and body.
The system should allow users to see upcoming events.
The system should allow users to create upcoming events which includes a title, description, location and dates.
The system should have 5-10 users, posts, announcements, and events so that it can be populated with data for the demo.
"""
module_name = "hi_neighbor.py"
class_name = "HiNeighbor"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
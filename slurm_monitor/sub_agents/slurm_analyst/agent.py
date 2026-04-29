"""HPC Environment Analyst sub-agent for querying Slurm status."""

from google.adk import Agent
import subprocess
from google.adk.agents import LlmAgent

from . import prompt

def run_sinfo(partition: str = "") -> str:
    """Gets the cluster status using the sinfo command.
    
    Args:
        partition: Optional partition name to filter the results (e.g., 'standard', 'gpu').
    """
    cmd = ["sinfo"]
    if partition:
        cmd.extend(["-p", partition])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running sinfo: {e.stderr}"
    except FileNotFoundError:
        return "Error: 'sinfo' command not found. Ensure this is running on a Slurm node."

def run_squeue(partition: str = "") -> str:
    """Gets the current job queue status using the squeue command.
    
    Args:
        partition: Optional partition name to filter the queue.
    """
    cmd = ["squeue"]
    if partition:
        cmd.extend(["-p", partition])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running squeue: {e.stderr}"
    except FileNotFoundError:
        return "Error: 'squeue' command not found. Ensure this is running on a Slurm node."

slurm_analyst_agent = LlmAgent(
    name="slurm_analyst_agent",
    model="gemini-2.5-pro",
    description="Analyzes the Slurm cluster environment and node status using tools like sinfo and squeue.",
    instruction=prompt.SLURM_ANALYST_PROMPT,
    output_key="cluster_environment_analysis_output",
    tools=[run_sinfo, run_squeue],
)
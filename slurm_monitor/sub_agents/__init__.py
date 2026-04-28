"""Package containing the various specialized sub-agents for the Slurm HPC Monitor."""

# Expose sub-agents here so they can be easily imported into agent.py
# e.g., from .sub_agents import env_analyst_agent
from .slurm_analyst.agent import env_analyst_agent

# As you continue migrating other agents, you can expose them here:
# from .data_analyst import data_analyst_agent
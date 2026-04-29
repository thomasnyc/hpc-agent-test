"""HPC Environment Coordinator: provide reasonable HPC environment strategies."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.hpc_env_analyst import hpc_env_analyst_agent
from .sub_agents.slurm_analyst import slurm_analyst_agent

MODEL = "gemini-2.5-pro"


hpc_coordinator = LlmAgent(
    name="hpc_coordinator",
    model=MODEL,
    description=(
        "guide users through a structured process to receive HPC "
        "advice by orchestrating a series of expert subagents."
    ),
    instruction=prompt.HPC_ENV_ANALYST_PROMPT,
    output_key="HPC_ENV_ANALYST_OUTPUT",
    tools=[
        AgentTool(agent=hpc_env_analyst_agent),
        AgentTool(agent=slurm_analyst_agent),
    ],
)

root_agent = hpc_coordinator
"""GCP Monitor sub-agent for querying Cloud Monitoring and Logging."""

from google.adk import Agent
from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro"

def get_gce_vm_status(project_id: str, zone: str = "") -> str:
    """Retrieves the status of GCE VMs used for HPC workloads.
    
    Args:
        project_id: The GCP project ID.
        zone: Optional GCP zone to filter by.
    """
    # TODO: Implement google-cloud-monitoring or google-cloud-compute logic here
    return f"Simulated output: Found active HPC VMs in project {project_id}."

def get_filestore_usage(project_id: str, location: str = "") -> str:
    """Retrieves the utilization of Filestore instances.
    
    Args:
        project_id: The GCP project ID.
        location: Optional GCP region/zone.
    """
    # TODO: Implement google-cloud-monitoring logic for Filestore capacity
    return f"Simulated output: Filestore instances operating within normal limits in {project_id}."

def query_hpc_logs(project_id: str, resource_type: str = "gce_instance") -> str:
    """Queries GCP Cloud Logging for recent HPC resource events or errors.
    
    Args:
        project_id: The GCP project ID.
        resource_type: The GCP resource type (e.g., 'gce_instance', 'filestore_instance').
    """
    # TODO: Implement google-cloud-logging logic here
    return f"Simulated output: No critical errors found in logs for {resource_type}."

gcp_monitor_agent = LlmAgent(
    name="gcp_monitor_agent",
    model="gemini-2.5-pro",
    description="Analyzes GCP monitoring and logging data to track HPC resources like GCE VMs and Filestore.",
    instruction=prompt.HPC_ENV_ANALYST_PROMPT,
    output_key="hpc_env_analyst_output",
    tools=[get_gce_vm_status, get_filestore_usage, query_hpc_logs],
)
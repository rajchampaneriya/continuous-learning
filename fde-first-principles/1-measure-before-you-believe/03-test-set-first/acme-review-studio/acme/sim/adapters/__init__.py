"""The only adapters a manifest may select."""
from .direct import AgentLoopAdapter, DirectAdapter, VersionBAdapter
from .http import HttpAdapter
from .orchestrated import DeclarativeAdapter, OrchestratedAdapter
from .team import MultiAgentAdapter
from .version_d import VersionDAdapter

ADAPTERS = {
    "studio-langgraph": OrchestratedAdapter,
    "spec-langgraph": DeclarativeAdapter,
    "lab-c3": AgentLoopAdapter,
    "offline": DirectAdapter,
    "lab-version-b": VersionBAdapter,
    "http-json": HttpAdapter,
    "team": MultiAgentAdapter,
    "lab-version-d": VersionDAdapter,
}

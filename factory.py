from typing import Any, Callable
from agent import Agent


agents: dict[str, Callable[..., Agent]] = {}


def register(agent_name: str, agent: Callable[..., Agent]) -> None:
    """Register a new game character type."""
    agents[agent_name] = agent


def unregister(agent_name: str) -> None:
    """Unregister a game character type."""
    agents.pop(agent_name, None)


def create(kwargs: dict[str, Any]) -> Agent:
    """Create a game character of a specific type, given JSON data."""
    agent_name = kwargs.pop("agent_name")
    try:
        agent = agents[agent_name]
    except KeyError:
        raise ValueError(f"unknown agent: {agent_name}") from None
    return agent(**kwargs)

import pytest
from pathlib import Path
from typing import Dict, Any, List
from src.utils.config_loader import load_config

ANALYST_CONFIG_PATH = Path("configs/agents/analyst.yml")

def test_analyst_config_exists() -> None:
    """
    Ensure the analyst.yml file exists.
    """
    assert ANALYST_CONFIG_PATH.exists(), f"{ANALYST_CONFIG_PATH} does not exist."


def test_load_analyst_config() -> None:
    """
    Test loading the analyst.yml configuration and verify required fields.
    """
    config: Dict[str, Any] = load_config(ANALYST_CONFIG_PATH)

    # The agent definition is under the top-level key "agent"
    assert "agent" in config, "Missing top-level 'agent' key"
    agent: Dict[str, Any] = config["agent"]

    # Top-level agent keys
    required_keys = ["name", "version", "description", "max_steps", "logging_level", "tools", "decision_logic"]
    for key in required_keys:
        assert key in agent, f"Missing '{key}' key in agent config"

    # Validate types
    assert isinstance(agent["name"], str)
    assert isinstance(agent["version"], float)
    assert isinstance(agent["description"], str)
    assert isinstance(agent["max_steps"], int)
    assert isinstance(agent["logging_level"], str)
    assert isinstance(agent["decision_logic"], str)

    # Validate tools
    tools: List[Dict[str, Any]] = agent["tools"]
    assert len(tools) > 0, "Agent config should define at least one tool"

    for tool in tools:
        required_tool_keys = ["name", "type", "tool_ref", "description"]
        for key in required_tool_keys:
            assert key in tool, f"Tool missing '{key}'"
            assert isinstance(tool[key], str)

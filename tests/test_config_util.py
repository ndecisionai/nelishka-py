import pytest
import yaml
from pathlib import Path
from typing import Tuple, Dict, Any
from src.utils.config_loader import load_config


@pytest.fixture
def sample_config_file(tmp_path: Path) -> Tuple[Path, Dict[str, Any]]:
    """
    Creates a temporary YAML config file for testing.

    Returns:
        Tuple[Path, dict]: Path to the temp YAML file and the expected config data.
    """
    config_data: Dict[str, Any] = {
        "agent": {
            "name": "analyst",
            "version": "1.0",
            "description": "Test agent",
            "tools": [
                {"name": "llm_context_pack", "type": "Tool"}
            ]
        }
    }
    file_path: Path = tmp_path / "test_config.yml"
    with open(file_path, "w") as f:
        yaml.dump(config_data, f)
    return file_path, config_data


def test_load_config(sample_config_file: Tuple[Path, Dict[str, Any]]) -> None:
    """
    Test loading a YAML configuration file and validating its structure.
    """
    file_path, expected_config = sample_config_file
    config: Dict[str, Any] = load_config(file_path)

    # Check that config is a dict
    assert isinstance(config, dict)

    # Check top-level keys
    assert "agent" in config

    # Check agent definition
    agent: Dict[str, Any] = config["agent"]
    assert agent["name"] == expected_config["agent"]["name"]
    assert agent["version"] == expected_config["agent"]["version"]
    assert agent["description"] == expected_config["agent"]["description"]

    # Check tools
    tools: list[Dict[str, Any]] = agent.get("tools", [])
    assert len(tools) == 1
    assert tools[0]["name"] == "llm_context_pack"
    assert tools[0]["type"] == "Tool"

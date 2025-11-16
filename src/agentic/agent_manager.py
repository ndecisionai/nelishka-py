import yaml
import importlib
from pathlib import Path
from typing import Dict, Optional, List, Callable, cast

from .config_models import AgentConfig, ToolConfig
from .types import AgentState
from .tool_protocol import ToolCallable
from .agent_protocol import AgentCallable


BASE_DIR = Path(__file__).resolve().parents[2]
AGENTS_CONFIG_DIR = BASE_DIR / "configs" / "agents"
TOOLS_CONFIG_DIR = BASE_DIR / "configs" / "tools"


class AgentManager:
    """
    Fully typed dynamic loader for agents & tools based on YAML configs.
    """

    def __init__(self) -> None:
        self.agent_configs: Dict[str, AgentConfig] = {}
        self.tool_configs: Dict[str, ToolConfig] = {}

        self.tools: Dict[str, ToolCallable] = {}
        self.agents: Dict[str, AgentCallable] = {}

        self._load_agent_configs()
        self._load_tool_configs()

        self._import_tools()
        self._import_agents()

    # ----------------------------------------------------
    # YAML load
    # ----------------------------------------------------
    def _load_agent_configs(self) -> None:
        for file in AGENTS_CONFIG_DIR.glob("*.yml"):
            with open(file, "r") as f:
                raw = yaml.safe_load(f)

            agent_cfg = AgentConfig(**raw["agent"])
            self.agent_configs[agent_cfg.name] = agent_cfg

    def _load_tool_configs(self) -> None:
        for file in TOOLS_CONFIG_DIR.glob("*.yml"):
            with open(file, "r") as f:
                raw = yaml.safe_load(f)

            tool_cfg = ToolConfig(**raw["tool"])
            self.tool_configs[tool_cfg.name] = tool_cfg

    # ----------------------------------------------------
    # Load tools dynamically
    # ----------------------------------------------------
    def _import_tools(self) -> None:
        for tool_name, _cfg in self.tool_configs.items():
            module_path = f"src.agentic.tools.{tool_name}"

            try:
                module = importlib.import_module(module_path)
            except ModuleNotFoundError:
                print(f"[WARN] Missing tool module: {module_path}")
                continue

            fn = getattr(module, f"{tool_name}_tool", None)

            if callable(fn):
                self.tools[tool_name] = fn  # type: ignore
            else:
                print(f"[WARN] Tool function `{tool_name}_tool` not found in {module_path}")

    # ----------------------------------------------------
    # Load agents dynamically
    # ----------------------------------------------------
    def _import_agents(self) -> None:
        for agent_name, cfg in self.agent_configs.items():
            role_module = f"src.agentic.agents.{cfg.name}"

            try:
                module = importlib.import_module(role_module)
            except ModuleNotFoundError:
                print(f"[WARN] Agent module missing: {role_module}")
                continue

            fn = getattr(module, f"{cfg.name}_agent", None)

            if callable(fn):
              typed_raw = cast(Callable[[AgentState, AgentConfig, Dict[str, ToolCallable]], AgentState], fn)
              wrapped = self._wrap_agent(typed_raw, cfg)
              self.agents[agent_name] = wrapped
            else:
              print(f"[WARN] Agent function `{cfg.name}_agent` missing in {role_module}")

    # ----------------------------------------------------
    # Wrap agent to inject config + tools
    # ----------------------------------------------------
    def _wrap_agent(
        self,
        fn: Callable[[AgentState, AgentConfig, Dict[str, ToolCallable]], AgentState],
        config: AgentConfig
    ) -> AgentCallable:

        def wrapped(state: AgentState) -> AgentState:
            tool_map: Dict[str, ToolCallable] = {}

            for t in config.tools:
                if t.tool_ref in self.tools:
                    tool_map[t.name] = self.tools[t.tool_ref]

            return fn(state, config, tool_map)

        return wrapped

    # ----------------------------------------------------
    # Public API
    # ----------------------------------------------------
    def get_agent(self, name: str) -> Optional[AgentCallable]:
        return self.agents.get(name)

    def list_agents(self) -> List[str]:
        return list(self.agents.keys())

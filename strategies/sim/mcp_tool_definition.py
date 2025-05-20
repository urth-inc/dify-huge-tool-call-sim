import json
from typing import List

from dify_plugin.entities.model.message import PromptMessageTool


def load_mcp_tool_definition():
    with open("./strategies/sim/mcp_tool_definition.json", "r") as f:
        data = json.load(f)

    prompt_tools: List[PromptMessageTool] = []
    for tool in data:
        prompt_tools.append(
            PromptMessageTool(
                name=tool["name"],
                description=tool["description"],
                parameters=tool["parameters"],
            )
        )

    return prompt_tools

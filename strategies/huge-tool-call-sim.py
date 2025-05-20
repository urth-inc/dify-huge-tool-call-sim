import logging

from collections.abc import Generator
from typing import Any
from pydantic import BaseModel

from dify_plugin.interfaces.agent import AgentModelConfig

from dify_plugin.entities.model.llm import LLMModelConfig, LLMResult, LLMResultChunk
from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.interfaces.agent import AgentStrategy

# from strategies.sim.prompt_history import load_prompt_history
from strategies.sim.history import get_history
from strategies.sim.mcp_tool_definition import load_mcp_tool_definition

stdio_logging_handler = logging.StreamHandler()
stdio_logging_handler.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.addHandler(stdio_logging_handler)
logger.setLevel(logging.INFO)


class BasicParams(BaseModel):
    model: AgentModelConfig


class HugeToolCallSimAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        params = BasicParams(**parameters)

        prompt_history = get_history()
        prompt_message_tools = load_mcp_tool_definition()

        chunks: Generator[LLMResultChunk, None, None] | LLMResult = (
            self.session.model.llm.invoke(
                prompt_messages=prompt_history,
                model_config=LLMModelConfig(**params.model.model_dump(mode="json")),
                tools=prompt_message_tools,
                stream=True,
            )
        )

        response = ""

        logger.info(f"🐛<type of chunks: {type(chunks)}")
        for chunk in chunks:
            response += chunk.delta.message.content

        logger.info(f"🐛<response: {response}")

        yield self.create_text_message(text=f"{response}")


# if __name__ == "__main__":
#     strategy = HugeToolCallSimAgentStrategy()
#     print(strategy.invoke({"prompt": "Hello, world!"}))

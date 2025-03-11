from __future__ import annotations as _annotations

import asyncio
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import logfire
from dotenv import load_dotenv

from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai import Agent, ModelRetry, RunContext

load_dotenv()
llm = os.getenv('LLM_MODEL', 'gpt-4o-mini')

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')


@dataclass
class Mem0Deps:
    memories: str


mem0_agent = Agent(
    OpenAIModel(llm),
    system_prompt=f'You are a helpful AI. Answer the question based on query and memories. The current date is: {datetime.now().strftime("%Y-%m-%d")}',
    deps_type=Mem0Deps,
    retries=2
)

@mem0_agent.system_prompt  
def add_memories(ctx: RunContext[str]) -> str:
    return f"\nUser Memories:\n{ctx.deps.memories}"

async def main():
    deps = Mem0Deps(memories="")
    
    result = await mem0_agent.run(
        'Greetings!', deps=deps
    )
    
    print('Response:', result.data)


if __name__ == '__main__':
    asyncio.run(main())
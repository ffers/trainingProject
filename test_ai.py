


import pytest

pytest.skip("integration example", allow_module_level=True)

dotenv = pytest.importorskip("dotenv")
load_dotenv = dotenv.load_dotenv
import os
load_dotenv()


from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
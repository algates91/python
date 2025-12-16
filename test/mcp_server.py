from fastmcp import FastMCP
from model import Task
import requests
import json

mcp = FastMCP("Test MCP Server", port=6000)

@mcp.tool
def get_tasks_tool() -> list[Task | None]:
    '''
    This tool is used to get all the tasks from backend
    
    :return: list of tasks
    :rtype: list[Task]
    '''
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQW5hbmQiLCJyb2xlIjoiaW50ZXJ2aWV3ZWUiLCJhY3RpdmUiOnRydWUsImV4cCI6MTc2ODQ1NDU5NH0.BD-hXtm5jgR2EYPZwGfFZowpN5qXiWMSFdOwIXrtPhc"
    header = {"Authorization":f"Bearer {token}"}
    response = requests.get("http://localhost:9000/tasks", headers=header)
    return json.loads(response.content)


if __name__ == "__main__":
    mcp.run(transport="http")
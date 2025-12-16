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
    token=""
    header = {"Authorization":f"Bearer {token}"}
    response = requests.get("http://localhost:9000/tasks", headers=header)
    return json.loads(response.content)


if __name__ == "__main__":
    mcp.run(transport="http")
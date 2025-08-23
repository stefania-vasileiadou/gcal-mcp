'''

server.py

MCP server setup

Author: Stefania Vassiliadou (Northwestern CE/CS '27)

'''

from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("gcal")

if __name__ == "__main__":
    mcp.run()
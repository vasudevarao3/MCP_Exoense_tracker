from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://expense-tracker-1812.fastmcp.app/mcp",
    name = "vasu server proxy"
)

if __name__== "__main__":
    mcp.run()


# Run the server - uv run fastmcp run proxy.py 
# Test the server - uv run fastmcp dev proxy.py

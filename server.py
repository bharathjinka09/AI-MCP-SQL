import sqlite3
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("PersistentMemory")

DB_PATH = "agent_memory.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )


@mcp.tool()
def store_memory(key: str, content: str) -> str:
    """Stores a piece of information to remember later."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO memories (key, content) VALUES (?, ?)", (key, content)
            )
        return f"Memory '{key}' saved successfully."
    except Exception as e:
        return f"Error saving memory: {str(e)}"


@mcp.tool()
def retrieve_memory(key: str) -> str:
    """Retrieves a specific memory by its key."""
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute("SELECT content FROM memories WHERE key = ?", (key,)).fetchone()
        return row[0] if row else "Memory not found."


@mcp.tool()
def list_memories() -> str:
    """Lists all stored memories with their keys."""
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT key FROM memories").fetchall()
        if rows:
            return "Stored Memories:\n" + "\n".join(f"- {row[0]}" for row in rows)
        else:
            return "No memories stored yet."

@mcp.tool()
def update_memory(key: str, new_content: str) -> str:
    """Updates an existing memory with new information."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("UPDATE memories SET content = ? WHERE key = ?", (new_content, key))
        if cursor.rowcount > 0:
            return f"Updated memory for '{key}' successfully."
        else:
            return f"No memory found with the key '{key}' to update."


@mcp.tool()
def delete_memory(key: str) -> str:
    """Deletes a specific memory from the database permanently."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("DELETE FROM memories WHERE key = ?", (key,))
        if cursor.rowcount > 0:
            return f"Memory '{key}' has been deleted."
        else:
            return f"Could not find a memory with the key '{key}' to delete."


if __name__ == "__main__":
    init_db()
    mcp.run()

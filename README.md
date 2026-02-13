# Steps to run the MCP server :-

## Prerequisites :-

Download Gemini Code Assist VS Code extension

Make sure that the gemini code extension is in agent mode

IMPORTANT - Reload VS Code after updating any settings to refresh

Use ``` /mcp ``` command to list all tools in chat 

Add this to .gemini/settings.json in C:/Users/Lenovo/.gemini:

```
{
  "mcpServers": {
    "my-persistent-memory": {
      "command": "C:/Users/Lenovo/Downloads/mcp_sql_project/venv/Scripts/python.exe",
      "args": ["C:/Users/Lenovo/Downloads/mcp_sql_project/server.py"],
      "env": {
        "PYTHONPATH": "C:/Users/Lenovo/Downloads/mcp_sql_project"
      }
    }
  }
}
```

## Prompts:- 

Test the full "CRUD" (Create, Read, Update, Delete) cycle:

Store: "Add key as project lead and content is Alex to db." (Uses store_memory)

Retrieve: "Who is my project lead?" (Uses retrieve_memory)

Fetch all: "List all memories" (Uses list_memories)

Update: "Actually, Alex left; update my project lead memory to say the lead is now Sarah." (Uses update_memory)

Delete: "I'm done with the project lead info, you can delete that memory now." (Uses delete_memory)


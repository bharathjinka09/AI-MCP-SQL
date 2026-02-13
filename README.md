# Steps to run the MCP server :-

## Prerequisites :-

Download Gemini Code Assist VS Code extension

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

Store: "Remember that my project lead is Alex." (Uses store_memory)

Retrieve: "Who is my project lead?" (Uses retrieve_memory)

Update: "Actually, Alex left; update my project lead memory to say the lead is now Sarah." (Uses update_memory)

Delete: "I'm done with the project lead info, you can delete that memory now." (Uses delete_memory)


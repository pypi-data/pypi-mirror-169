# Toolrunner
### _Automating standard procedure_
Toolrunner is a small python module created to automate commands/tools, collect their respective outputs into one place, and generally expedite the "initial triage" phase of malware analysis. It's basically just a big wrapper around the subprocess module. Configurations can be loaded from or saved to python dictionaries, making it easy to switch between whatever sets of tools are most applicable to the situation.
## Basic Usage
See [*documentation*](https://toolrunner.readthedocs.io/en/latest/)

Toolrunner's most practical use (and the inspiration behind its development) is starting/running the standard tools and processes one 
might typically employ during the static analysis of an exectutable. The alternative is manually clicking/running them all, redirecting 
outputs, copy/pasting file paths, typing commands, etc. Those clicks add up over time.

```py
import toolrunner
target_file = toolrunner.get_argv() # Drag/drop the file, retrieve path via argv[1]
tools = toolrunner.Tools(target_file, "tool_outputs") # Define output directory (CWD, otherwise)

tools.cli("capa details", r"C:\Users\IEUser\Desktop\capa.exe", ["-vv"])
tools.cli("floss strings", r"C:\Users\IEUser\Desktop\floss.exe")
tools.gui("IDA Pro", r"C:\Program Files\IDA Freeware 8.0\ida64.exe")
tools.gui("Detect it easy", r"C:\Users\IEUser\Desktop\ToolDownloads\die_win64_portable_3.06\die.exe")

tools.run_all() # GUI tools run first, and in their own process
tools.print_config()

input("\nPress enter to continue...") # So the console doesn't just immediatly exit
```
DetectItEasy and IDA Pro are loaded with our file; reports on the file's capabilities and strings are stored in */tool_outputs*.
The *print_config()* method prints the dictionary of the tool information we just manually provided in a readable format. So we can copy/paste that and perform the same actions like so:
```py
import toolrunner

static_cfg = {
        "cli" : {
                "capa summary" : ['C:\\Users\\IEUser\\Desktop\\capa.exe'],
                "capa details" : ['C:\\Users\\IEUser\\Desktop\\capa.exe', '-vv'],
                "floss strings" : ['C:\\Users\\IEUser\\Desktop\\floss.exe'],
        },
        "gui" : {
                "IDA Pro" : ['C:\\Program Files\\IDA Freeware 8.0\\ida64.exe'],
                "Detect it easy" : ['C:\\Users\\IEUser\\Desktop\\ToolDownloads\\die_win64_portable_3.06\\die.exe'],
        },
}

tools = toolrunner.Tools(toolrunner.get_argv(), "static_reports", config=static_cfg)
tools.run_all() 
input("\nPress enter to continue...") 
```
Dictionaries in this format can be used as the configuration for *toolrunner.Tools* objects, and edited to suit whatever your desires may be.

Linux equivilent [*here*](https://toolrunner.readthedocs.io/en/latest/usage.html)
## Known Issues & TODO
- If a tool changes the console's text color and doesn't change it back, it's just gonna stay that way
	- Use colorama
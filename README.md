# PyCharm SCP


## Description

It is an [**External Tool**](https://www.jetbrains.com/help/pycharm/configuring-third-party-tools.html) for PyCharm 
designed to transfer files between a local storage and a remote server. The purpose of this tool is similar to 
[**File Transfer**](https://www.jetbrains.com/help/pycharm/uploading-and-downloading-files.html) from Professional
Edition, but this project carries less functionality.


## Installation

1. Activate a virtual environment if necessary and install this library to your current Python environment: 

```bash
pip install git+ssh://git@github.com/ok-42/pycharm-scp.git
```

2. Add the external tool to PyCharm:

<details> <summary> Via GUI </summary>

- Open *Settings &mdash; Tools &mdash; External Tools*.
- Click *Add* button.
- Fill in the following fields:
  - Name: `SCP` (or any other name)
  - Program: `$ModuleSdkPath$`
  - Arguments: `-m pcscp $FilePathRelativeToProjectRoot$ $ProjectFileDir$`
  - Working directory: `$ProjectFileDir$`
- Click *OK*.
</details>

<details> <summary> Via PyCharm settings file </summary>

- Replace `USERNAME` and `PYCHARM` with actual values and open
  `C:\Users\USERNAME\AppData\Roaming\JetBrains\PYCHARM\settingsRepository\repository\tools\External Tools.xml`.
- Incorporate `<tool>` tag from [this file](examples/external_tools.xml) into settings file or paste the whole 
  `<toolSet>` tag if the settings file is empty. The final structure should contain single `<toolSet>` tag with 
  `<tool>` tag(s) nested:
```xml
<toolSet name="External Tools">
<tool> </tool>
<tool> </tool>
</toolSet> 
```
- Reload PyCharm.
</details>

3. (Optional) Assign a shortcut to the tool:

- Open *Settings &mdash; Keymap*.
- Expand *External Tools / External Tools* sections.
- Click twice on *SCP* tool (or another name if you chose it in the 2<sup>nd</sup> step).
- Select *Add Keyboard Shortcut*.
- Press the desired key combination. If it contains <kbd>Enter</kbd>, <kbd>Escape</kbd> or <kbd>Tab</kbd>, click 
  *Plus* button and select one.

4. Create a file named `pcscp.json` in the project root using [this template](examples/pcscp.json). The file should 
   be excluded from version control as it is intended for storing information on the local path on your machine, and 
   could disclose user and host names.

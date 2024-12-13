# PortaEXE - Portable EXE Maker

PortaEXE is a user-friendly tool for creating portable executables. With a simple GUI, it allows you to package an executable file along with its dependencies into a portable folder or a compressed ZIP file.

## Features

- Select an executable file (`.exe`) to package.
- Optionally include a dependencies folder for additional files required by the executable.
- Specify an output folder for the portable package.
- Automatically creates a ZIP file of the portable package for easy distribution.
- Clean and intuitive graphical user interface (GUI).

## How It Works

1. Select the executable (`.exe`) file that you want to make portable.
2. Optionally specify a folder containing dependencies (e.g., DLLs, resources) if required by the executable.
3. Choose the output folder where the portable package will be created.
4. Click the **Create Portable EXE** button to generate the portable package.
5. The tool creates a portable folder containing the executable and its dependencies, and then compresses it into a ZIP file.

## System Requirements

- **Operating System**: Windows 10 or later
- **Python Version**: Python 3.7 or later
- **Libraries**: 
  - `tkinter` (comes pre-installed with Python)
  - `shutil` and `zipfile` (built-in Python modules)

## License

PortaEXE is released under the MIT License.



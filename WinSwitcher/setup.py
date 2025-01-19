from cx_Freeze import setup, Executable

# Configure build options
build_exe_options = {
    "packages": ["os"],  # Add built-in Python packages
    "includes": [
        "RunPromptWrapper.MenuEntry",
        "RunPromptWrapper.RunPromptWrapper",
        "WinSwitcher.SwitcherMenu",
        "WinSwitcher.Window",
    ],
    "excludes": ["tkinter"],  # Exclude unused packages
    # Non-Python files
    "include_files": [("RunPromptWrapper/LICENSE", "LICENSE")],
    "zip_include_packages": "*",  # Include all packages in a zip archive
    "zip_exclude_packages": [],  # Exclude none
}

# Define the main executable
executables = [
    Executable(
        "WinSwitcher.py",
        target_name="WinSwitcher",  # Name of the final binary
        base=None  # No GUI base for Linux
    )
]

# Setup script
setup(
    name="WinSwitcher",
    version="1.0",
    description="WinSwitcher Application",
    options={"build_exe": build_exe_options},
    executables=executables,
)

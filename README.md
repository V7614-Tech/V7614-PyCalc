>⚠ False Positive Notice
Some antivirus programs (especially Avast, AVG, and similar) may incorrectly flag V7614 PyCalc as a virus.
This is a false positive caused by the way the program is packaged (Python + obfuscation + EXE bundling).
The program is safe to use — if flagged, please add it to your antivirus exceptions list.
For those with GitHub accounts, please:
Open an issue in the [Issues tab](https://github.com/V7614-Tech/V7614-PyCalc/issues) describing your antivirus and the detection.
Submit the file to your antivirus vendor’s false positive form to help whitelist it.
Thank you for helping keep V7614 PyCalc safe and accessible to all users. 💙

# V7614 PyCalc

*V7614 PyCalc* is a console-based calculator written in Python by [Vincent V7614](https://github.com/V7614), designed for Windows (and Linux with Wine).  
It features simple math support and continuing equations.

This is my first Python project! Releases may be a bit late if there are bugs that need fixing.  
V7614 PyCalc is a Python Script made with Python 3.13.0 that is packaged into a Windows `.exe` file!
Updates will be rolled out 3 times a week, specifically, Sunday, Wednesday, and Saturday, unless specified

---

## News!

I am proud to announce that V7614 PyCalc version 1.0.0 is finally out! This is a full-blown project now!

---

## ☑️ Requirements

**Minimum Requirements:**
- A Windows operating system, **or**
- Linux with Wine installed

**Recommended Requirements:**
- The latest version of Windows, **or**
- Linux with Wine

> 💡 **Note:** Wine is a compatibility layer for running Windows applications on Linux.  
> It is **not** installed by default or included with V7614 PyCalc. Unless your chosen Linux Distribution does not have Wine or any other compatibility layers installed yet (by you) or does not support Wine or those compatibility layers, sorry but V7614 PyCalc will not be able to run on your OS 

---

## 🚀 Installation Instructions

1. Make sure you're using **Windows** or **Linux**.
2. **(Linux only)** Ensure that **Wine** is installed.
3. Download the latest **non-beta** `V7614_PyCalc_X.X.X_setup.exe` release (unless you want to test beta versions).
4. Open the setup file.
5. (If your antivirus flags V7614 PyCalc) Add an exception for the setup file
6. Choose where to install V7614 PyCalc (you can do this with the destination being an external device for a portable install).
7. Choose whether you want to add a desktop and/or a start menu entry
8. Let the setup do it's thing.
9. (If your antivirus also flas `V7614PyCalc.exe`) Add an exception for `V7614PyCalc.exe`
10. Run V7614 PyCalc from the shortcut the setup added on the desktop, start menu entry, or directly from the directory you installed to (default is C:\<Program Files>\V7614\V7614)
11. Start calculating!

---

## 🐞 Known Bugs

1. **(FIXED) Invalid action input**
   - **Details:** If the calculator receives an invalid action selection, it will ask for the next number again instead of showing an error.
   - **Affected Versions:** `V7614 PyCalc 0.1.0`, `0.2.0`  
   - **Fixed?:** Yes, the fix for this bugis in `V7614 PyCalc 0.2.1`.  
   - **Workaround:** Double-check your action input before pressing `Enter` **or**, update to `V7614 PyCalc 0.2.1`.
---

2. **(FIXED) "Continue" bottleneck**
   - **Details:** The fix for `Known Bug 1.` in `V7614 PyCalc 0.2.1` bottlenecks the "continue" function of the calculator.
   - **Affected versions:** `V7614 PyCalc 0.2.1`
   - **Fixed?:** Yes, the fix for this bug is in the unreleased `V7614 PyCalc 1.0.0 Beta 1`. If you don't want to install a beta version, you can install the new update `V7614 PyCalc 1.0.0`.
   - **Workaround:** This is a bad one. There are **NO** workarounds for this bug. **or**, update to `V7614 PyCalc 1.0.0`.
---

Made with ❤️ by Vincent V7614 using Python.

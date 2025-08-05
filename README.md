#⚠ False Positive Notice!

>Some antivirus programs (especially Avast, AVG, and similar) may incorrectly flag V7614 PyCalc as a virus.
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

# 🚀 Installation Instructions for V7614 PyCalc

## Requirements
- **Windows** (native) or **Linux** (with Wine installed).
- macOS users: See notes below.

> 💡 **Note:** Wine is a compatibility layer for running Windows applications on Linux.  See how to install Wine on Linux below
> It is **not** installed by default or included with V7614 PyCalc. Unless your chosen Linux Distribution does not have Wine or any other compatibility layers installed yet (by you) or does not support Wine or those compatibility layers, sorry but V7614 PyCalc will not be able to run on your OS 

---

## 1️⃣ Download the latest stable release
- Grab the newest non-beta `V7614_PyCalc_X.X.X_setup.exe` from the [Releases page](https://github.com/V7614-Tech/V7614-PyCalc/releases).
- (You can grab a beta if you want to help test features early.)

## 2️⃣ Run the setup file
- Double-click the `.exe` installer.
- If Windows SmartScreen appears, click **More info** → **Run anyway**.

## 3️⃣ Handle antivirus warnings (if any)
- Some antivirus programs (especially Avast, AVG, etc.) may falsely flag V7614 PyCalc.
- Add an exception for the setup file if flagged.

## 4️⃣ Choose your installation options
- Pick your install location (**tip:** you can select an external drive for a portable install).
- Choose whether to add a Desktop shortcut and/or Start Menu entry.

## 5️⃣ Complete the installation
- Let the installer finish its work.
- If your antivirus flags `V7614PyCalc.exe`, add an exception for that file too.

## 6️⃣ Launch V7614 PyCalc
- Use the Desktop shortcut, Start Menu entry, or run it directly from the install folder:  
Default install location is below:
  ```
  C:\Program Files\V7614Tech\V7614 PyCalc\
  ```
- On Linux + Wine, run the `.exe` from your chosen install directory.

## 7️⃣ Start calculating! 🎉

---

# 🍷 Installing Wine on Linux

### Ubuntu / Debian / Linux Mint
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install wine64 wine32
```

### Fedora
```bash
sudo dnf install wine
```

### Arch Linux / Manjaro
```bash
sudo pacman -S wine
```

After installing, check Wine is installed:
```bash
wine --version
```

Run V7614 PyCalc with:
```bash
wine V7614PyCalc.exe
```

---

# 🍏 (For macOS Users) Compatibility with Mac OS

macOS does not natively support running Windows apps through Wine as easily as Linux.

Options:
- **Wine for macOS** (via [WineHQ](https://www.winehq.org) or PlayOnMac) — may be buggy or limited.
- **Virtual Machine** (recommended for full compatibility):
  - Parallels Desktop (paid)
  - VMware Fusion (free for personal use)
  - UTM (free, QEMU-based)
- **Boot Camp** (Intel Macs only) — install Windows alongside macOS.

Apple Silicon (M1/M2/M3/M4) Macs cannot use Boot Camp and require virtualization for Windows compatibility.
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

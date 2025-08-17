# ⚠ False Positive Notice!

> Some antivirus programs (especially Avast, AVG, and similar) may incorrectly flag V7614 PyCalc as a virus.  
> This is a **false positive** caused by the way the program is packaged (Python + obfuscation + EXE bundling).  
> The program is safe to use — if flagged, please add it to your antivirus exceptions list.

For those with GitHub accounts:  
- Open an issue in the [Issues tab](https://github.com/V7614-Tech/V7614-PyCalc/issues) describing your antivirus and the detection.  
- Submit the file to your antivirus vendor’s false positive form to help whitelist it.  

Thank you for helping keep V7614 PyCalc safe and accessible to all users. 💙

---

# 📝 Note to other people with a project name similar to PyCalc

V7614 PyCalc was originally called **Python Calculator**, made to help me master Python.  
I later shortened its name to **PyCalc**, and very recently rebranded again before the release on GitHub.  
It turns out the name was already used, so I rebranded it again.

**V7614 PyCalc and Chill Astro's PyCalc are two separate projects, and none of us copied each other.**  
I just had an idea while learning Python.  

Hope this clears up any confusion with other PyCalc projects.  

– Yours truly, Vincent V7614

---

# Note from the developer!

V7614 PyCalc's updates will be delayed because of schoolwork, sorry to have you waiting!
-Vincent V7614

---

# **V7614 PyCalc**

*V7614 PyCalc* is a console-based calculator written in Python by [Vincent V7614](https://github.com/V7614), designed for **Windows** (and **Linux with Wine**).  
It supports basic math operations and continuing equations.

This is my first Python project! Releases may be a bit late if bugs need fixing.  
V7614 PyCalc is made with **Python 3.13.0** and packaged into a Windows `.exe` file.  

**Update Schedule:** Sunday, and Saturday (unless specified otherwise).
---

## 🆕 News!

> 13th August 2025: V7614 PyCalc 1.1.0 will add **NATIVE** support for Debian/Ubuntu based distros, and coming with this is source code for V7614 PyCalc version 1.1.0 will be out as well, since after the rewrite the old code will be useless, so there it will be for people learning Python (V7614 PyCalc 2.0.0 won't get this treatment because by then, it is too complex for begginers and it's source code won't be open to the publis)

---

# 🚀 Installation Instructions

## Requirements

### For versions 0.1.0-1.0.0
- **Windows** 8/8.1 or higher (native)  
- **Linux** (with Wine installed)  
- **macOS users**: See the notes below.

---

### For future versions (1.1.0 and above)
- **Windows** 8/8.1 or higher (native)  
- **Linux** (Debian, Ubuntu, Mint, or any other Debian/Ubuntu based distros) (native)  
- **macOS users**: See the notes below.

> 💡 **Note:** Wine is a compatibility layer for running Windows apps on Linux. It is **not** installed by default.  
> If your Linux distro doesn’t have Wine (or support it), V7614 PyCalc will not run.

---

## 1️⃣ Download the latest stable release
- Grab the newest non-beta `V7614_PyCalc_X.X.X_setup.exe` from the [Releases page](https://github.com/V7614-Tech/V7614-PyCalc/releases).  
- You can grab a beta if you want to help test features early.

## 2️⃣ Run the setup file
- Double-click the `.exe` installer.  
- If Windows SmartScreen appears, click **More info** → **Run anyway**.

## 3️⃣ Handle antivirus warnings
- Some antivirus programs may falsely flag V7614 PyCalc.  
- Add an exception for the setup file if flagged.

## 4️⃣ Choose installation options
- Pick your install location (**tip:** you can select an external drive for a portable install).  
- Choose whether to add a Desktop shortcut and/or Start Menu entry.

## 5️⃣ Complete installation
- Let the installer finish.  
- If your antivirus flags `V7614PyCalc.exe`, add an exception for that file too.

## 6️⃣ Launch V7614 PyCalc
- Use the Desktop shortcut, Start Menu entry, or run it from the install folder:  
---

## 7️⃣ Start calculating! 🎉
---

# 🍷 Installing Wine on Linux

### Ubuntu / Debian / Linux Mint

sudo dpkg --add-architecture i386
sudo apt update
sudo apt install wine64 wine32

### Fedora

sudo dnf install wine

### Arch Linux / Manjaro

sudo pacman -S wine

### After installing, check:

wine --version
## Run V7614 PyCalc with:

wine V7614PyCalc.exe

# 🍏 macOS Compatibility
macOS does not natively support Windows apps through Wine as easily as Linux.

### Options:

Wine for macOS (via WineHQ or PlayOnMac) — may be buggy or limited.
Virtual Machine (recommended for full compatibility):
Parallels Desktop (paid)
VMware Fusion (free for personal use)
UTM (free, QEMU-based)
Boot Camp (Intel Macs only) — install Windows alongside macOS.
Apple Silicon (M1/M2/M3/M4) Macs cannot use Boot Camp and require virtualization for Windows.

# 🐞 Known Bugs

1. (FIXED) Invalid action input
Details: If the calculator receives an invalid action selection, it asks for the next number again instead of showing an error.
Affected Versions: 0.1.0, 0.2.0
Fixed: Yes, in 0.2.1
Workaround: Double-check your action input before pressing Enter, or update to 0.2.1.

2. (FIXED) "Continue" bottleneck
Details: The fix for Bug #1 in 0.2.1 slowed down the “continue” function.
Affected Versions: 0.2.1
Fixed: Yes, in 1.0.0 Beta 1 and 1.0.0
Workaround: None — update to 1.0.0.

Made with ❤️ by Vincent V7614 using Python.

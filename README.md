<div align="center">

# 🎛️ CECILIA 5 — Apple Silicon Port
### *The Acousmatic & Sound Design Toolbox, Natively Restored for Apple Silicon (ARM64)*

[![macOS Apple Silicon](https://img.shields.io/badge/macOS-Apple%20Silicon%20(arm64)-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DSP](https://img.shields.io/badge/DSP-Pyo%201.1-orange?style=for-the-badge)](https://github.com/belangeo/pyo)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
[![Version](https://img.shields.io/badge/Version-5.4.0%20(Silicon)-success?style=for-the-badge)](https://github.com)

<p align="center">
  <b>A faithful, native ARM64 release of classic Cecilia 5.4.0 for modern macOS (Sonoma, Sequoia, and beyond). Zero Rosetta overhead, native Apple Silicon DSP, and the authentic, untouched classic user experience.</b>
</p>

---

</div>

## 🌌 What is Cecilia?

Originally conceived in **1995 by Jean Piché** at Université de Montréal to replace entire studio racks of analog gear in a *musique concrète* environment, **Cecilia** is a legendary secret weapon among experimental composers, sound designers, and electronic music producers. Later rebuilt in Python by **Olivier Bélanger** using the [Pyo](https://github.com/belangeo/pyo) DSP engine, Cecilia allows musicians to sculpt sound using interactive, multi-breakpoint automation curves directly bound to synthesis and audio-processing algorithms.

With over 50 built-in modules spanning **granular time-stretching, spectral cross-synthesis, comb resonator banks, formant vocoding, chaotic accumulators, and multiband distortion**, Cecilia turns simple audio files into evolving, otherworldly sonic landscapes.

---

## ⚡ Why This Apple Silicon Port?

As Apple transitioned the Mac platform from Intel (x86_64) to Apple Silicon (M1/M2/M3/M4/M5) and deprecated older Python 2.x and 3.7 runtimes, Cecilia 5.4.0 became virtually unusable on modern macOS:
- **Architecture Mismatch**: Legacy Intel-only C-extensions and audio dylibs (`portaudio`, `libsndfile`, `pyo`) failed to load or crashed under Rosetta 2 emulation.
- **GUI Engine Incompatibilities**: Newer versions of macOS (Monterey, Ventura, Sonoma, Sequoia) broke legacy wxPython runtimes with sizer assertion aborts and window management crashes.
- **No Native Arm64 Builds**: Musicians and sound artists were left without a working build on modern Macs.

### What This Port Delivers:
- **100% Native ARM64 Execution**: No Rosetta translation required. The DSP audio engine runs directly on Apple Silicon cores with near-zero latency and high power efficiency.
- **Modern Python 3.11 Runtime**: Refactored packaging and execution to run reliably with Python 3.11, modern NumPy, and wxPython 4.2+.
- **Pure Classic Experience**: All original Cecilia 5.4.0 modules, GUI behaviors, interface layouts, and algorithms are strictly preserved exactly as intended by its original authors.
- **Standalone `.app` & `.dmg`**: Ready-to-use macOS application bundle packaged with all native arm64 shared libraries self-contained.

> [!NOTE]
> **Looking for modern workflow additions?**
> If you are looking for new features such as multi-level **Undo/Redo (`Cmd+Z`)**, a dedicated **Visual Panic Button**, macOS **Drag & Drop** audio loading, **Spotlight Quick Search (`Cmd+K`)**, and **"All Parameters" simultaneous curve randomizers**, check out the companion project: **[Cecilia 5 — Pro Edition](https://github.com/)**.

---

## 🚀 Download & Installation

### Option 1: Pre-Built Disk Image (Recommended)

1. Download **`Cecilia5-Silicon-arm64.dmg`** from the [Releases](https://github.com) page.
2. Open the DMG and drag **`Cecilia5.app`** into your **`/Applications`** folder.
3. Open Terminal and run the following command to clear Gatekeeper quarantine (standard for unsigned open-source audio software):
   ```bash
   xattr -cr /Applications/Cecilia5.app
   ```
4. Double-click `Cecilia5.app` to launch natively on Apple Silicon!

---

## 🎹 Keyboard Shortcuts & Cheatsheet

| Shortcut | Action | Description |
|---|---|---|
| <kbd>Space</kbd> | **Play / Pause** | Start or stop real-time audio playback |
| <kbd>Cmd</kbd> + <kbd>O</kbd> | **Open File** | Open a saved `.c5` project file |
| <kbd>Cmd</kbd> + <kbd>S</kbd> | **Save** | Save current project state |
| <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> | **Save As** | Save current project under a new name |
| <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> | **Random Module** | Open a randomly selected built-in module |
| <kbd>Cmd</kbd> + <kbd>B</kbd> | **Bounce to Disk** | Render output non-realtime directly to an uncompressed audio file |
| <kbd>Cmd</kbd> + <kbd>A</kbd> | **Select All** | Select all points on the active automation curve |
| <kbd>Cmd</kbd> + <kbd>W</kbd> | **Close Window** | Close the active module window |
| <kbd>Cmd</kbd> + <kbd>Q</kbd> | **Quit** | Exit Cecilia 5 |
| <kbd>Cmd</kbd> + <kbd>,</kbd> | **Preferences** | Configure audio interface, driver, sample rate & buffer size |

---

## 🧩 Built-in Module Arsenal

Cecilia 5 comes pre-loaded with over 50 specialized processing and synthesis modules:

| Category | Modules |
|---|---|
| **Spectral** | `AddResynth`, `BinModulator`, `BinWarper`, `CrossSynth`, `CrossSynth2`, `Morphing`, `Shifter`, `SpectralDelay`, `SpectralFilter`, `SpectralGate`, `SpectralWarper`, `Transpose`, `Vectral` |
| **Time & Granular** | `BeatMaker`, `DelayMod`, `Granulator`, `Particle`, `Pelletizer`, `Stutterer`, `UltimateGrainer`, `4Delays` |
| **Resonators & Verbs** | `ConvolutionReverb`, `Convolve`, `DetunedResonators`, `MatrixReverb`, `Resonators`, `WGuideBank` |
| **Synthesis** | `AdditiveSynth`, `Pulsar`, `StochGrains`, `StochGrains2`, `WaveScanSynth` |
| **Pitch & Harmonics** | `ChordMaker`, `FreqShift`, `Harmonizer`, `LooperBank`, `LooperMod`, `PitchLooper`, `RandomAccumulator` |
| **Filters** | `AMFMFilter`, `AutoModFilter`, `Binaural`, `BrickWall`, `MaskFilter`, `ParamEQ`, `Phaser`, `StateVar`, `StateVar2`, `Vocoder` |
| **Dynamics** | `Degrade`, `Distortion`, `DynamicsProcessor`, `FeedbackLooper`, `UpDistoRes`, `WaveShaper` |
| **Multiband** | `MultiBandBeatMaker`, `MultiBandDelay`, `MultiBandDisto`, `MultiBandFreqShift`, `MultiBandGate`, `MultiBandHarmonizer`, `MultiBandReverb` |

---

## 🛠️ Building From Source on macOS (Apple Silicon)

If you prefer to run or build Cecilia from source in a local virtual environment:

### Prerequisites
- macOS 12 Monterey or higher (tested on macOS 14 Sonoma & 15 Sequoia on M1/M2/M3/M4)
- Python 3.11+
- Xcode Command Line Tools (`xcode-select --install`)
- Homebrew packages: `portaudio`, `libsndfile`

```bash
# Install Homebrew audio libraries
brew install portaudio libsndfile
```

### Setup & Run
```bash
# Clone the repository
git clone https://github.com/your-username/cecilia5-silicon.git
cd cecilia5-silicon

# Create virtual environment with Python 3.11
python3.11 -m venv venv
source venv/bin/activate

# Upgrade packaging tools and install requirements
pip install --upgrade pip setuptools wheel
pip install numpy wxpython pyo

# Launch Cecilia 5
python Cecilia5.py
```

### Packaging into a Standalone `.app`
To bundle into an ARM64 standalone application bundle using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --noconfirm --clean cecilia5.spec
codesign --force --deep -s - "dist/Cecilia5.app"
```

---

## 📜 Credits & Acknowledgments

Cecilia is open-source software distributed under the **GNU General Public License v3**.

- **Original Creator & Concept**: Jean Piché (1995, Université de Montréal)
- **Architecture & Python Rewrite**: Olivier Bélanger ([Ajax Sound Studio](http://ajaxsoundstudio.com/software/cecilia/))
- **Module Design & QA**: Jean-Michel Dumas, Julie Delisle
- **Audio Engine**: Pyo by Olivier Bélanger
- **Apple Silicon Port**: Modernized for native ARM64 by Mirko and Antigravity.

---

<div align="center">
  <sub>Preserving acousmatic heritage and experimental audio tools for future generations of Mac users.</sub>
</div>

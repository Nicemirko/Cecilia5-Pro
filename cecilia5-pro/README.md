<div align="center">

# 🎛️ CECILIA 5 — PRO EDITION
### *The Acousmatic & Sound Design Powerhouse, Resurrected for Apple Silicon*

[![macOS Apple Silicon](https://img.shields.io/badge/macOS-Apple%20Silicon%20(arm64)-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pyo DSP](https://img.shields.io/badge/DSP-Pyo%201.1-orange?style=for-the-badge)](https://github.com/belangeo/pyo)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
[![Version](https://img.shields.io/badge/Version-5.5.0-success?style=for-the-badge)](https://github.com)
[![Vibe Coded Port](https://img.shields.io/badge/Port-Vibe%20Coded%20⚡-purple?style=for-the-badge)](https://github.com)

<p align="center">
  <b>A modernized, native ARM64 release of Cecilia 5 featuring multi-level Undo/Redo, unified All-parameter randomizers, Quick Search module palette, dedicated Panic emergency controls, and zero Rosetta overhead on macOS Sonoma & Sequoia.</b>
</p>

---

</div>

## 🌌 What is Cecilia?

Originally conceived in **1995 by Jean Piché** at Université de Montréal to replace entire studio racks of analog gear in a *musique concrète* environment, **Cecilia** has long been a legendary secret weapon among experimental composers, sound designers, and electronic music producers. Later rebuilt in Python by **Olivier Bélanger** using the [Pyo](https://github.com/belangeo/pyo) DSP engine, Cecilia allows musicians to sculpt sound using interactive, multi-breakpoint automation curves directly bound to synthesis and audio-processing algorithms.

With over 50 built-in modules spanning **granular time-stretching, spectral cross-synthesis, comb resonator banks, formant vocoding, chaotic accumulators, and multiband distortion**, Cecilia turns simple audio files into evolving sonic landscapes.

---

## ⚡ The "Vibe-Coded" Port Story

As macOS transitioned to Apple Silicon (M1/M2/M3/M4) and deprecated older Python 2/3.7 runtimes, Cecilia suffered severe bit rot:
- Broken C-extensions and audio dylibs (`portaudio`, `libsndfile`, `pyo`) refusing to load on ARM64.
- wxPython GUI crashes and memory leaks under macOS Sonoma and Sequoia.
- No native arm64 build existed, leaving sound designers stranded or wrestling with Rosetta emulation and broken dependencies.

This repository is a **100% vibe-coded resurrection**: an intensive agentic pair-programming overhaul that modernized every layer of the codebase:
- Recompiled and bundled **Pyo 1.1 + PortAudio + Libsndfile** natively for `arm64`.
- Upgraded the codebase to **Python 3.11** and **wxPython 4.2+** with modern memory management.
- Implemented the most requested usability features from decades of user feedback and community forums that were previously missing.

---

## ✨ Key Enhancements in v5.5.0 (Pro Edition)

### 🚨 Visual Panic Emergency Button
- **Instant DSP Silence**: High-visibility glowing **PANIC** button positioned directly beside the transport controls (Play & Record).
- Immediately stops runaway resonant filters, feedback loops, and stuck voices, resetting audio streams and flashing bright red on engagement (<kbd>Esc</kbd> key or click).

### 📂 Native macOS Drag & Drop Workflow
- **Instant Audio Sample Import**: Drag and drop any audio file (`.wav`, `.aif`, `.aiff`, `.flac`, `.ogg`, `.mp3`) directly from macOS Finder onto the application window, input file selectors, or sampler widgets to immediately load, parse, and analyze it with zero dialog navigation.
- **Project & Module Loading**: Drag any `.c5` project file or module from Finder directly onto the graph canvas or the macOS Dock icon to instantly load and compile the module and its automation curves.

### ↩️ Multi-Level Undo / Redo (`Cmd+Z` / `Cmd+Shift+Z`)
- True non-destructive undo and redo history for all grapher curve edits, point movements, and randomizations.
- Protected by deep-copy snapshotting to eliminate data drift and mathematical range clipping.

### 🎲 Unified "All Parameters" Randomization
- Select **"All"** in the parameter dropdown menu to randomize every automation curve simultaneously!
- **Stochastic Generator**: Randomizes all parameters with independent, non-identical seeds and distributions (`Gaussian`, `Uniform`, `Weibull`, `Beta`, `Drunk`, `Repeater`).
- **Waveform Generator**: Generates synchronized yet distinct waveforms (`Sine`, `Square`, `Triangle`, `Sawtooth`, `Sinc`, `Pulse`, `Bi-Pulse`) across all parameters with phase and harmonic offsets.
- **Process Transformer**: Applies independent jitter, scatter, comp/expand, and smoothing across all parameters at once.

### ⚡ Instant Visual & DSP Refresh
- Fixed the legacy bug where automation curves only redrew on canvas after switching parameters a second time.
- Curves and DSP slider graphs now update on screen and in the audio engine on the very first click of **Apply**.

### 🔍 Quick Search Module Palette (`Cmd+K`)
- Spotlight-style fuzzy search popup right above the `Modules` menu.
- Rapidly filter and open any of the 50+ modules without browsing nested subfolders.

### 🎨 Retina & Modern macOS Polish
- Smooth anti-aliased curves, rounded transport badges, modern dark theme accents, and toggle-to-close generator palettes.

---

## 🚀 Download & Installation

### Option 1: Pre-Built Disk Image (Recommended)

1. Download **`Cecilia5-Pro-Silicon-arm64.dmg`** from the [Releases](https://github.com) page.
2. Open the DMG and drag **`Cecilia5-Pro.app`** into your **`/Applications`** folder.
3. Open Terminal and run the following command to clear Gatekeeper quarantine (standard for open-source audio tools):
   ```bash
   xattr -cr /Applications/Cecilia5-Pro.app
   ```
4. Double-click `Cecilia5-Pro.app` to launch natively on Apple Silicon!

---

## 🎹 Keyboard Shortcuts & Cheatsheet

| Shortcut | Action | Description |
|---|---|---|
| <kbd>Cmd</kbd> + <kbd>K</kbd> | **Quick Search** | Open instant fuzzy finder for all modules |
| <kbd>Cmd</kbd> + <kbd>Z</kbd> | **Undo** | Revert last automation curve change |
| <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd> | **Redo** | Restore previously reverted change |
| <kbd>Space</kbd> | **Play / Pause** | Start or stop audio playback |
| <kbd>Esc</kbd> | **Panic Stop** | Emergency mute DSP audio engine and reset |
| <kbd>Cmd</kbd> + <kbd>O</kbd> | **Open File** | Open a saved `.c5` project |
| <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> | **Random Module**| Open a randomly selected built-in module |
| <kbd>Cmd</kbd> + <kbd>B</kbd> | **Bounce to Disk**| Render output directly to an uncompressed audio file |
| <kbd>Cmd</kbd> + <kbd>A</kbd> | **Select All** | Select all points on the active automation curve |
| <kbd>Cmd</kbd> + <kbd>,</kbd> | **Preferences** | Configure audio interface, sample rate & buffer size |

---

## 🧩 Built-in Module Arsenal

Cecilia 5 comes pre-loaded with over 50 specialized processing and synthesis modules:

| Category | Modules |
|---|---|
| **Spectral** | `AddResynth`, `BinModulator`, `BinWarper`, `CrossSynth`, `CrossSynth2`, `Morphing`, `Shifter`, `SpectralDelay`, `SpectralFilter`, `SpectralGate`, `SpectralWarper`, `Transpose`, `Vectral` |
| **Time & Granular** | `BeatMaker`, `DelayMod`, `Granulator`, `Particle`, `Pelletizer`, `Stutterer`, `UltimateGrainer`, `4Delays` |
| **Resonators & Verbs**| `ConvolutionReverb`, `Convolve`, `DetunedResonators`, `MatrixReverb`, `Resonators`, `WGuideBank` |
| **Synthesis** | `AdditiveSynth`, `Pulsar`, `StochGrains`, `StochGrains2`, `WaveScanSynth` |
| **Pitch & Harmonics** | `ChordMaker`, `FreqShift`, `Harmonizer`, `LooperBank`, `LooperMod`, `PitchLooper`, `RandomAccumulator` |
| **Filters** | `AMFMFilter`, `AutoModFilter`, `Binaural`, `BrickWall`, `MaskFilter`, `ParamEQ`, `Phaser`, `StateVar`, `StateVar2`, `Vocoder` |
| **Dynamics** | `Degrade`, `Distortion`, `DynamicsProcessor`, `FeedbackLooper`, `UpDistoRes`, `WaveShaper` |
| **Multiband** | `MultiBandBeatMaker`, `MultiBandDelay`, `MultiBandDisto`, `MultiBandFreqShift`, `MultiBandGate`, `MultiBandHarmonizer`, `MultiBandReverb` |

---

## 🐛 Known Bugs

- **Transport Panic / Clocker Hover Glitch**: Hovering directly over the Transport Panic button on macOS may cause the Panic button and adjacent minute counter to visually flicker or temporarily disappear until clicked or re-hovered. This is purely cosmetic: triggering Panic (via <kbd>Esc</kbd> or click), playback timing, and all DSP functions remain 100% operational.

---

## 🛠️ Building From Source on macOS

If you want to run or hack on Cecilia directly in a Python virtual environment:

### Prerequisites
- macOS 12 Monterey or higher (tested on macOS 14 Sonoma & 15 Sequoia on M1/M2/M3/M4)
- Python 3.11+
- Xcode Command Line Tools (`xcode-select --install`)
- Homebrew packages: `portaudio`, `libsndfile`

### Setup Environment
```bash
# Clone the repository
git clone https://github.com/your-username/cecilia5-pro.git
cd cecilia5-pro

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip setuptools wheel
pip install numpy wxpython pyo

# Launch Cecilia 5
python Cecilia5.py
```

### Packaging into a Standalone `.app`
```bash
pip install pyinstaller
pyinstaller --noconfirm --clean cecilia5.spec
codesign --force --deep -s - "dist/Cecilia5-Pro.app"
```

---

## 📜 Credits & Acknowledgments

Cecilia is open-source software distributed under the **GNU General Public License v3**.

- **Original Creator & Concept**: Jean Piché (1995, Université de Montréal)
- **Architecture & Python Rewrite**: Olivier Bélanger ([Ajax Sound Studio](http://ajaxsoundstudio.com/software/cecilia/))
- **Module Design & QA**: Jean-Michel Dumas, Julie Delisle
- **Audio Engine**: Pyo by Olivier Bélanger
- **Apple Silicon Port & 2026 Pro Edition**: Vibe-coded port and modernized by Mirko and Antigravity.

---

<div align="center">
  <sub>Made with ⚡ and deep love for acousmatic music, sound sculpture, and experimental audio.</sub>
</div>

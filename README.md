# Once-Human-Piano
Once Human Piano Midi Player

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/drastraea/Once-Human-Piano.git
cd Once-Human-Piano
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
For Python virtual environments :
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required Python packages using requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage
### Command-Line Arguments (Optional)
--file : Path to the MIDI file you want to play.
--pitch : Optional pitch modulation (integer value to adjust pitch).

### Run the Script
To run the script and play a MIDI file, use:
```bash
python OnceHuman.py --file path/to/your/file.mid
```
Or, if you do not provide the --file argument, you can use the code below and a file dialog will open to select a MIDI file:
```bash
python OnceHuman.py
```

### Example
```bash
python OnceHuman.py --file song.mid --pitch 2
```
This command will play song.mid with a pitch modulation of 2.

## Dependencies
- mido: MIDI file handling.
- pydirectinput: Simulates keyboard input.
- easygui: File selection dialog.
- colorama: Text color in terminal.

- 

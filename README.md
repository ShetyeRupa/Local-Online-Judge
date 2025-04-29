# Local Online Judge System

A Python-based programming evaluation tool that compiles and runs code against test cases.

## 🚀 Features
- Supports Python, C, C++, and Java
- Automated test case verification
- Detailed error reporting
- Cross-platform support

## 📦 Prerequisites
- Python 3.8+
- For C/C++: [MinGW-w64](https://www.mingw-w64.org/) (Windows) or `build-essential` (Linux)
- For Java: JDK 8+

## 🛠️ Installation
```bash
git clone https://github.com/yourusername/local-online-judge.git
cd local-online-judge
mkdir -p problems solutions/{python,c,cpp,java} temp
```

## 📂 Project Structure
```
.
├── problems/          # Problem definitions (JSON)
├── solutions/        # User code submissions
├── temp/             # Compiled binaries
└── local_online_judge.py  # Main program
```

## 🧩 Creating Problems
1. Add a JSON file in `problems/` (e.g., `1.json`):
```json
{
  "id": "1",
  "title": "Sum of Two Numbers",
  "test_cases": [
    {"input": "2 3", "output": "5"},
    {"input": "-1 5", "output": "4"}
  ]
}
```

## 🖥️ Usage
```bash
python local_online_judge.py
```
Follow the interactive menu to:
1. Select problem
2. Choose language
3. View results

## 🐛 Troubleshooting
| Issue | Solution |
|-------|----------|
| GCC not found | Add MinGW to PATH |
| Java class error | Ensure filename matches class name |
| Test failures | Check whitespace in outputs |

## 📜 License
MIT © [Rupali Ravindra Shetye]

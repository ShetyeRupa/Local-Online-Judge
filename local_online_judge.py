# Ruplai Ravindra Shetye
import os
import json
import subprocess
from pathlib import Path
import shutil
import sys

class OnlineJudge:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.problems_dir = self.base_dir / "problems"
        self.solutions_dir = self.base_dir / "solutions"
        self.temp_dir = self.base_dir / "temp"
        
        self.problems = {}  # Initialize problems dict
        self.load_problems()  # Load problems

    def load_problems(self):
        """Load all problem definitions from JSON files"""
        try:
            if not self.problems_dir.exists():
                raise FileNotFoundError(f"Problems directory not found: {self.problems_dir}")
            
            for json_file in self.problems_dir.glob("*.json"):
                with open(json_file, 'r') as f:
                    problem = json.load(f)
                    self.problems[problem['id']] = problem
                    
            print(f"Loaded {len(self.problems)} problems")
        except Exception as e:
            print(f"Error loading problems: {str(e)}")
            self.problems = {}

    def list_problems(self):
        """List all available problems"""
        if not self.problems:
            print("\nNo problems found. Check the problems directory.")
            return
        
        print("\nAvailable Problems:")
        for pid, pdata in sorted(self.problems.items(), key=lambda x: int(x[0])):
            print(f"{pid}. {pdata['title']}")

    def run_code(self, problem_id, language):
        problem = self.problems.get(problem_id)
        if not problem:
            return [False] * len(problem.get('test_cases', []))
        
        try:
            if language == 'python':
                cmd = ['python', f"{self.solutions_dir}/python/problem{problem_id}.py"]
                
            elif language == 'c':
                # Use absolute paths for reliability
                c_src_path = self.solutions_dir / 'c' / f'problem{problem_id}.c'
                c_exe_path = self.temp_dir / 'c' / f'problem{problem_id}.exe'
                
                # Create directory if needed
                c_exe_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Find GCC (try multiple common locations)
                gcc_paths = [
                    r"C:\mingw64\bin\gcc.exe",
                    r"C:\MinGW\bin\gcc.exe",
                    "gcc"  # Try system PATH as last resort
                ]
                
                gcc_found = None
                for path in gcc_paths:
                    if Path(path).exists() or path == "gcc":
                        gcc_found = path
                        break
                
                if not gcc_found:
                    print("Error: GCC compiler not found. Please install MinGW-w64.")
                    return [False] * len(problem['test_cases'])
                
                # Compile with detailed error reporting
                compile_result = subprocess.run(
                    [gcc_found, str(c_src_path), '-o', str(c_exe_path), 
                    '-Wall', '-Wextra', '-g'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                # Print compilation output
                if compile_result.stdout:
                    print("\nCOMPILATION OUTPUT:")
                    print(compile_result.stdout)
                if compile_result.stderr:
                    print("\nCOMPILATION ERRORS:")
                    print(compile_result.stderr)
                
                if compile_result.returncode != 0:
                    print(f"C Compilation failed with exit code {compile_result.returncode}")
                    return [False] * len(problem['test_cases'])
                
                if not c_exe_path.exists():
                    print("Error: Executable was not created after compilation")
                    return [False] * len(problem['test_cases'])
                
                cmd = [str(c_exe_path)]
                
            elif language == 'cpp':
                # Use absolute paths
                cpp_src_path = self.solutions_dir / 'cpp' / f'problem{problem_id}.cpp'
                cpp_exe_path = self.temp_dir / 'cpp' / f'problem{problem_id}.exe'
                
                # Create directory if needed
                cpp_exe_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Find G++ (try multiple common locations)
                gpp_paths = [
                    r"C:\mingw64\bin\g++.exe",
                    r"C:\MinGW\bin\g++.exe",
                    "g++"  # Try system PATH as last resort
                ]
                
                gpp_found = None
                for path in gpp_paths:
                    if Path(path).exists() or path == "g++":
                        gpp_found = path
                        break
                
                if not gpp_found:
                    print("Error: G++ compiler not found. Please install MinGW-w64.")
                    return [False] * len(problem['test_cases'])
                
                # Compile with detailed error reporting
                compile_result = subprocess.run(
                    [gpp_found, str(cpp_src_path), '-o', str(cpp_exe_path),
                    '-Wall', '-Wextra', '-std=c++17', '-g'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                # Print compilation output
                if compile_result.stdout:
                    print("\nCOMPILATION OUTPUT:")
                    print(compile_result.stdout)
                if compile_result.stderr:
                    print("\nCOMPILATION ERRORS:")
                    print(compile_result.stderr)
                
                if compile_result.returncode != 0:
                    print(f"C++ Compilation failed with exit code {compile_result.returncode}")
                    return [False] * len(problem['test_cases'])
                
                if not cpp_exe_path.exists():
                    print("Error: Executable was not created after compilation")
                    return [False] * len(problem['test_cases'])
                
                cmd = [str(cpp_exe_path)]
                
            elif language == 'java':
                java_dir = self.temp_dir / 'java'
                if java_dir.exists():
                    shutil.rmtree(java_dir)
                java_dir.mkdir(parents=True, exist_ok=True)
                
                compile_result = subprocess.run([
                    'javac',
                    '-verbose',
                    '-encoding', 'UTF-8',
                    '-d', str(java_dir),
                    str(self.solutions_dir/'java'/f'Problem{problem_id}.java')
                ], capture_output=True, text=True)
                
                print("\nCOMPILATION OUTPUT:")
                print(compile_result.stdout)
                if compile_result.stderr:
                    print("COMPILATION ERRORS:")
                    print(compile_result.stderr)
                
                cmd = [
                    'java',
                    '-cp', str(java_dir.absolute()),
                    f"Problem{problem_id}"
                ]
                
            else:
                raise ValueError(f"Unsupported language: {language}")

            results = []
            for case in problem['test_cases']:
                try:
                    input_data = case['input'].strip() + '\n'
                    process = subprocess.run(
                        cmd,
                        input=input_data,
                        text=True,
                        capture_output=True,
                        timeout=5
                    )
                    
                    user_output = process.stdout.strip()
                    expected_output = case['output'].strip()
                    results.append(user_output == expected_output)
                    
                    print(f"\nTest Case:")
                    print(f"Input: {input_data.strip()}")
                    print(f"Expected: {expected_output}")
                    print(f"Received: {user_output}")
                    if process.stderr:
                        print(f"Errors: {process.stderr.strip()}")
                        
                except subprocess.TimeoutExpired:
                    print(f"Timeout on: {case['input']}")
                    results.append(False)
                    
            return results
            
        except Exception as e:
            print(f"Execution failed: {str(e)}", file=sys.stderr)
            return [False] * len(problem['test_cases'])

    def evaluate(self):
        """Main evaluation flow"""
        self.list_problems()
        
        if not self.problems:
            return
            
        try:
            problem_id = input("\nEnter Problem ID: ").strip()
            if problem_id not in self.problems:
                print("Invalid problem ID!")
                return
                
            print("\nAvailable Languages:")
            print("1. Python\n2. C\n3. C++\n4. Java")
            lang_choice = input("Select language (1-4): ").strip()
            languages = {'1': 'python', '2': 'c', '3': 'cpp', '4': 'java'}
            language = languages.get(lang_choice, 'python')
            
            results = self.run_code(problem_id, language)
            passed = sum(results)
            total = len(results)
            
            print(f"\nResults: {passed}/{total} test cases passed")
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")

if __name__ == "__main__":
    judge = OnlineJudge()
    judge.evaluate()
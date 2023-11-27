# Project Report

## Git Hooks

This was a valuable lesson in determining how git hooks would work in a team environment. Which brings me to the first lesson.

The first lesson and arguably most important lesson I learned in a team environment was that git hooks are not uploaded to the repo with other files. Instead after researching, I determined the best course of action is to create a seperate folder and upload the hook there with instructions on how to copy the file to the .git/hook directory in order to use the git hook.

Git Hooks Implementation Steps:
- Determine what the git hook would run (bandit)
- Determine how the results would be saved (csv file)
- Determine how to pass implementating the git hook to other team members (readme)
- Display that the implementation was running (echo that the scan occured)

The Git Hook information can be found in the /GitHooksFiles folder in the repository. 

## Fuzz

This was valuable practice in implementing Fuzzing into a Python application via GitHub actions.

Fuzzing implementation steps:
- created a method to return a random integer, float, or None type.
- created a method that returns a random YAML file name from blns.json
- created a method that returns randomly nested dictionaries filled with random data types.
- passed the randomly generated data to several methods in parser.py. This is repeated 5 times.
- display the errors caught using try exception blocks.
- created a workflow file in order to implement the fuzzing when a new push or pull is done.

Lessons Learned:
    
    I learned that Fuzzing is an important way to ensure you have a stable and safe application. I was also able to learn that it can help you catch any new errors you might introduce after the initial tests by implementing it through GitHub actions.
  
## Forensics

This was a valuable exercise in determining 'what to log' in an application.

Logging implementation steps:

- Created a logger implementation similar to Workshop 8, but made the dated file name dynamic to always use the current date rather than a hard coded date.
- Added logging in main.py to log scanner, dataframe, and analysis count outputs for data changes.
- Added logging in scanner.py to log scanned directories and filepaths for data access.
- Added logging in parser.py to log the yaml content being read into the software to log data access.

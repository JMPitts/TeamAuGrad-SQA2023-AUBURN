# Project Report

## Git Hooks

The first lesson I learned was that git hooks are not uploaded to the repo with other files. Instead after googling, I determined the best course of action is to create a seperate folder and upload the hook there with instructions on how to copy the file to the .git/hook directory in order to use the git hook.

## Fuzz

## Forensics

This was a valuable exercise in determining 'what to log' in an application.

Logging implementation steps:

- Created a logger implementation similar to Workshop 8, but made the dated file name dynamic to always use the current date rather than a hard coded date.
- Added logging in main.py to log scanner, dataframe, and analysis count outputs for data changes.
- Added logging in scanner.py to log scanned directories and filepaths for data access.
- Added logging in parser.py to log the yaml content being read into the software to log data access.

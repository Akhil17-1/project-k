# Challenges and Issues

## Issue 1: Large Log File Size
- **Problem**: The log_collector.log file exceeded GitHub's file size limit of 100 MB, causing push errors.
- **Solution**: Implemented a mechanism to limit the log file size to 100 MB by splitting logs into chunks and deleting the oldest logs when the limit is reached.

## Issue 2: BSON Document Size Limit
- **Problem**: BSON document size exceeded MongoDB's limit of 16 MB, causing insertion errors.
- **Solution**: Modified the log_collector.py script to split large log documents into smaller chunks before inserting them into MongoDB.

## Issue 3: Log File Not Found
- **Problem**: Certain log files (e.g., network.log, firewall.log) were not found, causing errors in agent.py.
- **Solution**: Added error handling to skip missing log files and continue processing.

## Issue 4: Git Repository Cleanup
- **Problem**: Needed to remove large files from the Git repository to comply with GitHub's size limits.
- **Solution**: Used BFG Repo-Cleaner to strip large files from the repository history and cleaned up with git reflog and git gc.

## Ongoing Challenges
- **Optimization**: Continuously optimizing the log collection and processing scripts for better performance and reliability.
- **Error Handling**: Improving error handling within scripts to ensure robustness and stability.
- **Documentation**: Keeping documentation up-to-date with ongoing developments and changes.

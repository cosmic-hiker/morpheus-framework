#!/usr/bin/env python3

"""
Morpheus Framework Setup Script
Cross-platform setup for the Morpheus Framework AI development workflow
"""

import os
import sys
import shutil
from pathlib import Path
import urllib.request
import ssl
class Colors:
    if os.name == 'nt':  # Windows
        try:
            import colorama
            colorama.init()
            RED = '\033[31m'
            GREEN = '\033[32m'
            YELLOW = '\033[33m'
            BLUE = '\033[34m'
            RESET = '\033[0m'
        except ImportError:
            RED = GREEN = YELLOW = BLUE = RESET = ''
    else:  # Unix/Linux/Mac
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        RESET = '\033[0m'

def print_status(message):
    print(f"{Colors.GREEN}✅ {message}{Colors.RESET}")

def print_warning(message):
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.RESET}")

def print_error(message):
    print(f"{Colors.RED}❌ {message}{Colors.RESET}")

def print_info(message):
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.RESET}")

def detect_git_repo():
    """Check if we're in a git repository"""
    if Path(".git").exists():
        print_info("Git repository detected")
        return True
    else:
        print_warning("Not in a git repository - that's fine, continuing anyway")
        return False

def get_ai_tool_choice():
    """Interactive AI tool selection"""
    print()
    print_info("Which AI tool would you like to configure Morpheus for?")
    print()
    print("1) Cline")
    print("2) Roo")
    print("3) Cursor") 
    print("4) Claude Projects")
    print("5) Other (manual setup)")
    print("6) Skip tool configuration")
    print()
    
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print_warning("Please enter a number between 1 and 6")
        except KeyboardInterrupt:
            print()
            print_warning("Setup cancelled by user")
            sys.exit(0)
        except EOFError:
            print()
            print_warning("Setup cancelled")
            sys.exit(0)

def configure_ai_tool(choice, rules_file):
    """Configure AI tool based on user choice"""
    tool_configs = {
        '1': {
            'name': 'Cline',
            'dir': '.clinerules',
            'file': 'morpheus-rules.md'
        },
        '2': {
            'name': 'Roo',
            'dir': Path('.roo') / 'rules',
            'file': 'morpheus-rules.md'
        },
        '3': {
            'name': 'Cursor',
            'dir': Path('.cursor') / 'rules',
            'file': 'morpheus-rules.md'
        }
    }
    
    if choice in tool_configs:
        config = tool_configs[choice]
        print_info(f"Configuring for {config['name']}...")
        
        # Create directory if it doesn't exist
        config_dir = Path(config['dir'])
        config_dir.mkdir(parents=True, exist_ok=True)
        
        if not config_dir.exists():
            print_info(f"Created {config_dir} directory")
        
        # Copy rules file
        dest_file = config_dir / config['file']
        shutil.copy2(rules_file, dest_file)
        print_status(f"{config['name']} configuration complete")
        return config['name'], True  # Return tuple: (tool_name, rules_copied)
        
    elif choice == '4':
        print_info("For Claude Projects:")
        print("1. Open your Claude.ai Projects")
        print("2. Go to your project settings")
        print("3. Copy the content from morpheus-rules.md into 'Project instructions'")
        print()
        print_warning("Manual configuration required for Claude Projects")
        return "Claude Projects (manual setup required)", False
        
    elif choice == '5':
        print()
        print_info("Manual setup instructions:")
        print("Copy morpheus-rules.md to your AI tool's configuration location:")
        print("  • Cline: .clinerules/morpheus-rules.md")
        print("  • Roo: .roo/rules/morpheus-rules.md")
        print("  • Cursor: .cursor/rules/morpheus-rules.md")
        print("  • Claude Projects: Copy content to project instructions")
        print("  • Other tools: Check your tool's documentation for rules/config location")
        print()
        return "Manual", False
        
    elif choice == '6':
        print_warning("Skipping tool configuration")
        print("You can configure your AI tool later by copying morpheus-rules.md to the appropriate location")
        return "Skipped", False
    
    # Fallback case (shouldn't reach here, but just in case)
    return "Unknown", False

def should_cleanup_rules_file(rules_file, ai_tool_configured, rules_copied):
    """Ask user if they want to clean up the rules file from project root"""
    # Only offer cleanup if:
    # 1. Rules were successfully copied to AI tool config
    # 2. The rules file exists in current directory
    # 3. User didn't choose manual/skip options
    
    if not rules_copied or ai_tool_configured in ["Manual", "Skipped"]:
        print_info(f"DEBUG: Skipping cleanup - copied: {rules_copied}, tool: {ai_tool_configured}")
        return False
    
    if not Path(rules_file).exists():
        print_info(f"DEBUG: Rules file {rules_file} doesn't exist")
        return False
    
    # Check if this looks like the framework directory 
    # Look for multiple framework-specific files together
    framework_indicators = [
        Path("README.md").exists() and Path("morpheus-setup.py").exists(),
        Path(".git").exists() and "morpheus-framework" in str(Path.cwd())
    ]
    
    if any(framework_indicators):
        print_info("Detected framework directory - keeping rules file for reference")
        return False
    
    print()
    print_info(f"The rules file '{rules_file}' has been copied to your AI tool's configuration.")
    
    while True:
        try:
            response = input("Would you like to remove it from the project root to keep things tidy? (y/N): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no', '']:
                return False
            else:
                print_warning("Please enter 'y' for yes or 'n' for no")
        except (KeyboardInterrupt, EOFError):
            print()
            return False

def create_brief_template():
    """Create the brief.md template"""
    brief_content = '''# Project Brief

## What I Want to Build
[Describe your project idea - can be as simple as "A todo app" or as detailed as you like]

## Core Features (Optional)
1. [Main feature 1]
2. [Main feature 2]
3. [Additional features...]

## Success Criteria (Optional)
[How you'll know the project is successful]

## Technical Preferences (Optional)
- Framework: [preference or "no preference"]
- Database: [preference or "no preference"]
- Hosting: [preference or "no preference"]

## Context & Constraints (Optional)
[Timeline, team size, performance requirements, etc.]

---
*Fill out this brief and start working with your AI assistant to begin using Morpheus Framework*
'''
    
    morpheus_dir = Path('.morpheus')
    brief_file = morpheus_dir / 'brief.md'
    
    if not brief_file.exists():
        with open(brief_file, 'w', encoding='utf-8') as f:
            f.write(brief_content)
        print_status("Created .morpheus/brief.md template")
    else:
        print_info(".morpheus/brief.md already exists - keeping your existing version")

def create_context_template():
    """Create the initial context.md"""
    context_content = '''# Project Context

## Current Focus
[Project setup and initial planning]

## Key Decisions Made
- **Framework Setup**: Morpheus Framework configured - [Date]

## Project Status
- ✅ **Completed**: Initial project structure setup
- 🔄 **In Progress**: Project brief definition
- 📋 **Next**: Begin development based on brief

## Tech Stack & Architecture
[To be determined based on project brief]

## Important Patterns & Discoveries
[Will be updated as development progresses]

## Brief Alignment Check
**Last reviewed**: [Date]
**Status**: 📋 Needs brief completion
**Notes**: Project brief needs to be filled out to begin development
'''
    
    morpheus_dir = Path('.morpheus')
    context_file = morpheus_dir / 'context.md'
    
    if not context_file.exists():
        with open(context_file, 'w', encoding='utf-8') as f:
            f.write(context_content)
        print_status("Created initial .morpheus/context.md")
    else:
        print_info(".morpheus/context.md already exists - keeping your existing version")

def create_gitignore():
    """Create or update .gitignore with Morpheus entries"""
    gitignore_content = '''# Morpheus Framework  
morpheus-rules.md

# Dependencies
node_modules/
venv/
.env

# Build outputs
dist/
build/
*.pyc
__pycache__/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
    
    gitignore_file = Path('.gitignore')
    
    if gitignore_file.exists():
        # Check if Morpheus entries already exist
        with open(gitignore_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'morpheus-rules.md' not in content:
            with open(gitignore_file, 'a', encoding='utf-8') as f:
                f.write('\n# Morpheus Framework\nmorpheus-rules.md\n')
            print_status("Added Morpheus entries to .gitignore")
        else:
            print_info(".gitignore already contains Morpheus entries")
    else:
        with open(gitignore_file, 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        print_status("Created .gitignore with Morpheus Framework entries")

def main():
    """Main setup function"""
    print("🔮 Morpheus Framework Setup")
    print("==========================")
    print()

    rules_file_name = "morpheus-rules.md"
    rules_file_path = Path(rules_file_name)
    rules_url = "https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-rules.md"

    if not rules_file_path.exists():
        print_info(f"'{rules_file_name}' not found locally.")
        print_info(f"Attempting to download from {rules_url}...")
        try:
            # Create a default SSL context (helps with some environments)
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            with urllib.request.urlopen(rules_url, context=context) as response, open(rules_file_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            print_status(f"Successfully downloaded '{rules_file_name}'.")
        except Exception as e:
            print_error(f"Failed to download '{rules_file_name}': {e}")
            print_info("Please manually download it from the repository and place it in the current directory.")
            print_info("Repository: https://github.com/cosmic-hiker/morpheus-framework")
            sys.exit(1)
    else:
        print_status(f"Found '{rules_file_name}' locally.")
        
    # Detect git repository
    detect_git_repo()
    
    # Interactive AI tool selection and configuration
    choice = get_ai_tool_choice()
    ai_tool_configured, rules_copied = configure_ai_tool(choice, rules_file_name) # Use rules_file_name here
    
    print_info(f"DEBUG: Tool configured: '{ai_tool_configured}', Rules copied: {rules_copied}")
    
    # Set up project structure
    print_info("Setting up project structure...")
    
    # Create .morpheus directory
    morpheus_dir = Path('.morpheus')
    morpheus_dir.mkdir(exist_ok=True)
    
    # Create template files
    create_brief_template()
    create_context_template()
    
    # Create .gitignore
    create_gitignore()
    
    # Ask about cleaning up rules file
    print_info(f"DEBUG: Checking cleanup for tool: '{ai_tool_configured}', copied: {rules_copied}")
    if should_cleanup_rules_file(rules_file_path, ai_tool_configured, rules_copied): # Use rules_file_path
        try:
            os.remove(rules_file_path) # Use rules_file_path
            print_status(f"Removed {rules_file_name} from project root") # Use rules_file_name for message
        except OSError as e:
            print_warning(f"Could not remove {rules_file}: {e}")
    else:
        print_info("DEBUG: Cleanup was not offered or declined")
    
    # Success message
    print()
    print("🎉 Morpheus Framework Setup Complete!")
    print("====================================")
    print()
    
    if ai_tool_configured not in ["Skipped", "Manual"]:
        print_status(f"Configured for {ai_tool_configured}")
    
    print_status("Project structure created:")
    print("   📁 .morpheus/ - Framework documentation and context")
    print("   📋 .morpheus/brief.md - Define your project vision here")
    print("   📝 .morpheus/context.md - Current project state")
    
    print()
    print("🚀 Next Steps:")
    print("1. Edit .morpheus/brief.md to describe what you want to build")
    print("2. Say 'start' to your AI assistant to begin")
    print("3. Your AI will guide you through the Morpheus Framework!")
    print()
    
    if ai_tool_configured in ["Skipped", "Manual"]:
        print_warning("Remember to configure your AI tool with the Morpheus rules")
    
    print_info("Read more: https://github.com/cosmic-hiker/morpheus-framework")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print_warning("Setup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print()
        print_error(f"Setup failed with unexpected error: {e}")
        sys.exit(1)

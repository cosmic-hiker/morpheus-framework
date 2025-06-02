#!/bin/bash

# Morpheus Framework Setup Script
# Automatically configures the Morpheus Framework for your AI development workflow

set -e  # Exit on any error

echo "🔮 Morpheus Framework Setup"
echo "=========================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if we're in a git repository (optional)
if [ -d ".git" ]; then
    print_info "Git repository detected"
else
    print_warning "Not in a git repository - that's fine, continuing anyway"
fi

# Download Morpheus rules file
print_info "Downloading Morpheus Framework rules..."
if command -v curl >/dev/null 2>&1; then
    curl -s -o morpheus-rules.md https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-rules.md
    if [ $? -eq 0 ]; then
        print_status "Rules downloaded successfully"
    else
        print_error "Failed to download rules file"
        exit 1
    fi
elif command -v wget >/dev/null 2>&1; then
    wget -q -O morpheus-rules.md https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-rules.md
    if [ $? -eq 0 ]; then
        print_status "Rules downloaded successfully"
    else
        print_error "Failed to download rules file"
        exit 1
    fi
else
    print_error "Neither curl nor wget found. Please install one of them."
    exit 1
fi

# Interactive AI tool selection
echo ""
print_info "Which AI tool would you like to configure Morpheus for?"
echo ""
echo "1) Cline"
echo "2) Roo" 
echo "3) Cursor"
echo "4) Claude Projects"
echo "5) Other (manual setup)"
echo "6) Skip tool configuration"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        print_info "Configuring for Cline..."
        if [ ! -d ".clinerules" ]; then
            mkdir -p .clinerules
            print_info "Created .clinerules directory"
        fi
        cp morpheus-rules.md .clinerules/
        AI_TOOL_CONFIGURED="Cline"
        print_status "Cline configuration complete"
        ;;
    2)
        print_info "Configuring for Roo..."
        if [ ! -d ".roo/rules" ]; then
            mkdir -p .roo/rules
            print_info "Created .roo/rules directory"
        fi
        cp morpheus-rules.md .roo/rules/
        AI_TOOL_CONFIGURED="Roo"
        print_status "Roo configuration complete"
        ;;
    3)
        print_info "Configuring for Cursor..."
        if [ ! -d ".cursor/rules" ]; then
            mkdir -p .cursor/rules
            print_info "Created .cursor/rules directory"
        fi
        cp morpheus-rules.md .cursor/rules/
        AI_TOOL_CONFIGURED="Cursor"
        print_status "Cursor configuration complete"
        ;;
    4)
        print_info "For Claude Projects:"
        echo "1. Open your Claude.ai Projects"
        echo "2. Go to your project settings"
        echo "3. Copy the content from morpheus-rules.md into 'Project instructions'"
        echo ""
        print_warning "Manual configuration required for Claude Projects"
        AI_TOOL_CONFIGURED="Claude Projects (manual setup required)"
        ;;
    5)
        echo ""
        print_info "Manual setup instructions:"
        echo "Copy morpheus-rules.md to your AI tool's configuration location:"
        echo "  • Cline: .clinerules/morpheus-rules.md"
        echo "  • Roo: .roo/rules/morpheus-rules.md"
        echo "  • Cursor: .cursor/rules/morpheus-rules.md"
        echo "  • Claude Projects: Copy content to project instructions"
        echo "  • Other tools: Check your tool's documentation for rules/config location"
        echo ""
        AI_TOOL_CONFIGURED="Manual"
        ;;
    6)
        print_warning "Skipping tool configuration"
        echo "You can configure your AI tool later by copying morpheus-rules.md to the appropriate location"
        AI_TOOL_CONFIGURED="Skipped"
        ;;
    *)
        print_warning "Invalid choice. Skipping tool configuration."
        AI_TOOL_CONFIGURED="Skipped"
        ;;
esac

# Create basic project structure
print_info "Setting up project structure..."

# Create .morpheus directory
mkdir -p .morpheus

# Create brief.md template if it doesn't exist
if [ ! -f ".morpheus/brief.md" ]; then
    cat > .morpheus/brief.md << 'EOF'
# Project Brief

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
EOF
    print_status "Created .morpheus/brief.md template"
else
    print_info ".morpheus/brief.md already exists - keeping your existing version"
fi

# Create initial context.md
if [ ! -f ".morpheus/context.md" ]; then
    cat > .morpheus/context.md << 'EOF'
# Project Context

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
EOF
    print_status "Created initial .morpheus/context.md"
else
    print_info ".morpheus/context.md already exists - keeping your existing version"
fi

# Create .gitignore entries if needed
if [ -f ".gitignore" ]; then
    if ! grep -q "morpheus-rules.md" .gitignore; then
        echo "" >> .gitignore
        echo "# Morpheus Framework" >> .gitignore
        echo "morpheus-rules.md" >> .gitignore
        print_status "Added Morpheus entries to .gitignore"
    fi
else
    cat > .gitignore << 'EOF'
# Morpheus Framework  
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
EOF
    print_status "Created .gitignore with Morpheus Framework entries"
fi

# Clean up downloaded rules file from project root
rm morpheus-rules.md
print_status "Cleaned up temporary files"

echo ""
echo "🎉 Morpheus Framework Setup Complete!"
echo "===================================="
echo ""

if [ "$AI_TOOL_CONFIGURED" != "Skipped" ] && [ "$AI_TOOL_CONFIGURED" != "Manual" ]; then
    print_status "Configured for $AI_TOOL_CONFIGURED"
fi

print_status "Project structure created:"
echo "   📁 .morpheus/ - Framework documentation and context"
echo "   📋 .morpheus/brief.md - Define your project vision here"
echo "   📝 .morpheus/context.md - Current project state"

echo ""
echo "🚀 Next Steps:"
echo "1. Edit .morpheus/brief.md to describe what you want to build"
echo "2. Say 'start' to your AI assistant to begin"
echo "3. Your AI will guide you through the Morpheus Framework!"
echo ""

if [ "$AI_TOOL_CONFIGURED" = "Skipped" ] || [ "$AI_TOOL_CONFIGURED" = "Manual" ]; then
    print_warning "Remember to configure your AI tool with the Morpheus rules"
fi

print_info "Read more: https://github.com/cosmic-hiker/morpheus-framework"
echo ""
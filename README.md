# 🔮 Morpheus Framework
## Adaptive AI Development Workflow

> *"There is a difference between knowing the path and walking the path."* - Morpheus

An intelligent, self-improving development workflow that adapts to your project's complexity and learns from your patterns. Built for AI coding assistants like Cline, Roo, Cursor, and Claude.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Tools](https://img.shields.io/badge/AI%20Tools-Cline%20%7C%20Roo%20%7C%20Cursor%20%7C%20Claude-green.svg)](#supported-ai-tools)

## ⚡ Quick Start: One-Liner Setup

The easiest way to get started is to run the setup script directly in your project directory. The script will download `morpheus-rules.md` if needed.

**For Linux/macOS (bash/zsh):**
Open your terminal, navigate to your project's root directory, and run:
```bash
curl -sSL https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-setup.py | python3
```

**For Windows (PowerShell):**
Open PowerShell, navigate to your project's root directory, and run:
```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-setup.py -OutFile morpheus-setup.py; python morpheus-setup.py; Remove-Item morpheus-setup.py
```
*(This command downloads the script, runs it with Python, and then removes the downloaded script file.)*

After running the setup script:
1.  **Follow the interactive prompts** to configure Morpheus for your AI tool.
2.  **Edit `.morpheus/brief.md`** to describe what you want to build.
3.  **Start coding with your AI assistant** – It will now use Morpheus Framework patterns!

## 🧠 How It Works

### Confidence-Based Collaboration
Your AI assistant explicitly states confidence and adapts behavior:

- **≥90% Confidence**: "I'll proceed with implementing the login system using JWT authentication..."
- **75-89% Confidence**: "I'm ~80% confident about this approach. Let me confirm: you want user profiles with avatar uploads, correct?"
- **<75% Confidence**: "I need guidance on the payment integration. Should we use Stripe, PayPal, or something else?"

### Adaptive Project Structure
The framework automatically scales based on your project complexity:

#### Simple Projects
```
your-project/
├── README.md          
├── .morpheus/
│   ├── brief.md       # Your project vision
│   └── context.md     # Current state & decisions
└── src/
```

#### Standard Projects  
```
your-project/
├── README.md
├── .morpheus/
│   ├── brief.md       # Your project vision
│   ├── context.md     # Current state & decisions
│   ├── planning.md    # Architecture & tech decisions
│   └── tasks.md       # Feature backlog & progress
└── src/
```

#### Complex Projects
```
your-project/
├── README.md
├── .morpheus/
│   ├── brief.md       # Your project vision
│   ├── context.md     # Active work & recent changes
│   ├── planning.md    # Architecture & tech stack
│   ├── tasks.md       # Detailed task management
│   ├── patterns.md    # System patterns & decisions
│   ├── learning.md    # Workflow improvements
│   └── journal/       # Session logs & decisions
└── src/
```

## 📝 Writing Your Brief

Start with a `brief.md` file describing your project:

### Simple Project Example
```markdown
# Project Brief

## What I Want to Build
A simple todo app where I can add, complete, and delete tasks.
```

### Standard Project Example
```markdown
# Project Brief

## What I Want to Build
A habit tracking app with user accounts, daily check-ins, progress charts, and streak tracking.

## Core Features
1. User registration and authentication
2. Create and manage habits
3. Daily check-in system
4. Progress visualization with charts
5. Streak counting and achievements
```

### Complex Project Example
```markdown
# Project Brief

## What I Want to Build
A full e-commerce platform with product management, shopping cart, payment processing, and admin dashboard.

## Core Features
1. User management (customers and admins)
2. Product catalog with categories and search
3. Shopping cart and checkout process
4. Payment processing (Stripe integration)
5. Order management and tracking
6. Admin dashboard with analytics
7. Inventory management
8. Email notifications

## Technical Preferences
- Framework: React with Next.js
- Database: PostgreSQL
- Authentication: NextAuth.js
- Hosting: Vercel

## Success Criteria
- Handle 1000+ concurrent users
- Sub-2 second page load times
- PCI DSS compliant payment processing
- Mobile-responsive design
```

## 🔧 Alternative Setup Methods

While the one-liner setup is recommended, you can also use these methods:

### 1. Clone the Repository (for developers or to get all framework files)
```bash
# Clone the repository
git clone https://github.com/cosmic-hiker/morpheus-framework.git
cd morpheus-framework 

# Navigate to your actual project directory
# cd /path/to/your/project

# Then run the setup script from the cloned location, or copy morpheus-setup.py 
# and morpheus-rules.md to your project and run it there:
python3 /path/to/cloned/morpheus-framework/morpheus-setup.py 
# or if copied:
# python3 morpheus-setup.py
```
The script will guide you through configuration.

### 2. Manual Download and Setup
1.  **Download Files**:
    *   Download `morpheus-setup.py`
    *   Download `morpheus-rules.md`
    *   (Both available at `https://github.com/cosmic-hiker/morpheus-framework`)
2.  **Place in Your Project**: Put both files in the root of your project directory.
3.  **Run Setup Script**:
    ```bash
    python3 morpheus-setup.py # or python morpheus-setup.py on Windows
    ```
4.  **If not running the script, manually configure**:
    *   **Place `morpheus-rules.md` in your AI tool's configuration directory**:
        *   **Cline**: `.clinerules/morpheus-rules.md`
        *   **Roo**: `.roo/rules/morpheus-rules.md`
        *   **Cursor**: `.cursor/rules/morpheus-rules.md`
        *   **Claude Projects**: Copy content of `morpheus-rules.md` into project instructions.
    *   **Create project structure**:
   
   **Unix/Linux/Mac:**
   ```bash
   mkdir -p .morpheus
   touch .morpheus/brief.md .morpheus/context.md
   ```
   
   **Windows Command Prompt:**
   ```cmd
   mkdir .morpheus
   type nul > .morpheus\brief.md
   type nul > .morpheus\context.md
   ```
   
   **Windows PowerShell:**
   ```powershell
   New-Item -ItemType Directory -Force -Path .morpheus
   New-Item -ItemType File -Path .morpheus\brief.md
   New-Item -ItemType File -Path .morpheus\context.md
   ```

## 🎯 Key Features

- **📝 Natural Start**: Just describe what you want to build in `brief.md`
- **🤖 Smart Assessment**: AI evaluates project complexity automatically
- **🔄 Adaptive Structure**: Framework scales with your needs
- **🛡️ Proactive Quality Standards**: Enforces security, testing, performance, and maintainability best practices (e.g., 500-line rule, refactoring prompts, idempotency).
- **🗣️ Structured Communication**: Clear protocols for AI confidence levels, special triggers, and request handling.
- **📚 Memory Preserved**: Maintains context across AI sessions with structured updates.
- **🔧 Tool Agnostic**: Works with any AI coding assistant.
- **📈 Self-Improving**: Learns from your patterns, suggests process improvements, and proactively reflects on persistent challenges.

## 🛠️ Supported AI Tools {#supported-ai-tools}

| Tool | Configuration Location |
|------|----------------------|
| **Cline** | `.clinerules/morpheus-rules.md` |
| **Roo** | `.roo/rules/morpheus-rules.md` |
| **Cursor** | `.cursor/rules/morpheus-rules.md` |
| **Claude Projects** | Copy to project instructions |

## 💡 Examples

### First Interaction Flow
```
User: start

AI: I found your .morpheus/brief.md! Let me read it...

**Confidence: 85%** - Based on "weather app", I assess this as a 
Standard complexity project because it likely needs:
- API integration (weather service)
- Location handling
- Data visualization
- Multiple views

Should I:
A) Use your brief as-is and proceed
B) Refine the brief together first
C) Start with a fresh detailed discussion

Also, does "Standard complexity" sound right for your vision?
```

### Development Session
```
AI: **Confidence: 92%** - I'll implement the weather data fetching service.
I'll use the OpenWeatherMap API as planned and add proper error handling 
for network failures and invalid locations.

[Implements feature]

I've updated .morpheus/context.md with the new API integration patterns and 
added the completed weather service to our task list. The service handles 
rate limiting and caches responses for 10 minutes as discussed.

Next up: Should we work on the location search component or the weather 
display cards?
```

## 🏗️ Development Standards

The framework enforces quality standards automatically, guided by `morpheus-rules.md`:

### Code Quality Highlights
- **Maintainable Modularity**: E.g., Max 500 lines per file, with proactive refactoring suggestions for oversized or complex existing code.
- **Security-First**: Never hardcode credentials, validate all inputs, be mindful of common vulnerabilities (XSS, SQLi, IDORs), and check dependency security.
- **Test-Driven**: Write tests before implementation (happy path, edge cases, failures), considering unit, integration, and UI interaction tests as appropriate.
- **Performance-Conscious**: Implement caching, efficient algorithms, and consider scalability.
- **Idempotent Operations**: Strive for idempotency in scripts and operations where practical.

### AI Behavior Standards Highlights
- **Confidence Transparency**: Always state confidence level and adapt behavior accordingly.
- **Structured Request Handling**: Clarify vague requests effectively.
- **Human Collaboration**: Seek guidance when uncertain or for critical decisions (architecture, security, performance).
- **Context Preservation**: Update documentation (`context.md`, etc.) with structured, reviewable changes.
- **Brief Alignment**: Keep work aligned with project vision and flag deviations or needs for brief updates.

### Quality Validation
Before any significant implementation:
- [ ] Requirements clear (confidence ≥75%)
- [ ] Security implications assessed  
- [ ] Performance impact considered
- [ ] Test strategy defined

## 🔮 Philosophy

### Human-AI Partnership
Morpheus treats AI as a thoughtful partner, not just a code generator. It establishes clear communication patterns that scale from simple tasks to complex architectural decisions.

### Adaptive Intelligence
Rather than imposing rigid processes, the framework adapts to your project's actual complexity and learns from your specific patterns to improve collaboration over time.

### Vision Preservation
Keeps your project aligned with the original vision in `brief.md` while allowing natural evolution through conscious, tracked decisions.

## 🚀 Advanced Features

### Self-Improving Workflow
The framework learns from your patterns:
- Identifies effective collaboration patterns.
- Suggests process improvements and proactively reflects on persistent challenges.
- Adapts to your coding style and preferences.
- Evolves quality standards based on your projects (with human approval).

### Session Memory
Maintains context across AI sessions:
- Key decisions and rationale
- Successful patterns and anti-patterns
- Current project status and next steps
- Important discoveries and learnings

### Working Modes
- **Plan Mode**: Architecture, design, high-level decisions
- **Act Mode**: Implementation, debugging, testing

## 🤝 Contributing

Found an improvement? Morpheus is designed to evolve:

- **🐛 Issues**: Report bugs or suggest features
- **💡 Patterns**: Share successful workflow patterns
- **🔧 Improvements**: Suggest framework enhancements
- **📚 Examples**: Contribute project examples

## 📜 License

MIT License - Use freely, contribute back improvements.

---

**Ready to revolutionize your AI development workflow?** Start with the [One-Liner Setup](#-quick-start-one-liner-setup) and create your `.morpheus/brief.md`!

# 🔮 Morpheus Framework
## Adaptive AI Development Workflow

> *"There is a difference between knowing the path and walking the path."* - Morpheus

An intelligent, self-improving development workflow that adapts to your project's complexity and learns from your patterns. Built for AI coding assistants like Cline, Roo, Cursor, and Claude.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Tools](https://img.shields.io/badge/AI%20Tools-Cline%20%7C%20Roo%20%7C%20Cursor%20%7C%20Claude-green.svg)](#setup)

## ⚡ Quick Start

1. **Download and run setup**:
   ```bash
   curl -sSL https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-setup.sh | bash
   ```

2. **Create your project brief**:
   ```bash
   # The setup script creates .morpheus/brief.md template
   nano .morpheus/brief.md  # Describe what you want to build
   ```

3. **Start coding with your AI assistant** - It will now use Morpheus Framework patterns!

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

## 🔧 Setup

### Automatic Setup (Recommended)
```bash
# Interactive setup - choose your AI tool
curl -sSL https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-setup.sh | bash
```

The setup script will:
1. Download Morpheus Framework rules
2. Let you choose your AI tool (Cline, Roo, Cursor, Claude, etc.)
3. Configure the rules in the correct location
4. Create initial project structure
5. Generate template files

### Manual Setup
1. **Download the rules file**:
   ```bash
   curl -O https://raw.githubusercontent.com/cosmic-hiker/morpheus-framework/main/morpheus-rules.md
   ```

2. **Place it in your AI tool's configuration**:
   - **Cline**: Copy to `.clinerules/morpheus-rules.md`
   - **Roo**: Copy to `.roo/rules/morpheus-rules.md`
   - **Cursor**: Copy to `.cursor/rules/morpheus-rules.md`
   - **Claude Projects**: Copy content to project instructions

3. **Create project structure**:
   ```bash
   mkdir -p .morpheus
   touch .morpheus/brief.md .morpheus/context.md
   ```

## 🎯 Key Features

- **📝 Natural Start**: Just describe what you want to build in `brief.md`
- **🤖 Smart Assessment**: AI evaluates project complexity automatically
- **🔄 Adaptive Structure**: Framework scales with your needs
- **🛡️ Quality Built-in**: Security, testing, and performance standards
- **📚 Memory Preserved**: Maintains context across AI sessions
- **🔧 Tool Agnostic**: Works with any AI coding assistant
- **📈 Self-Improving**: Learns from your patterns

## 🛠️ Supported AI Tools

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

The framework enforces quality standards automatically:

### Code Quality
- **500-line rule**: Max 500 lines per file (forces good modular design)
- **Security-first**: Never hardcode credentials, validate all inputs
- **Test-driven**: Write tests before implementation
- **Performance-conscious**: Implement caching and efficient algorithms

### AI Behavior Standards
- **Confidence transparency**: Always state confidence level
- **Human collaboration**: Seek guidance when uncertain
- **Context preservation**: Update documentation after changes
- **Brief alignment**: Keep work aligned with project vision

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
- Identifies effective collaboration patterns
- Suggests process improvements
- Adapts to your coding style and preferences
- Evolves quality standards based on your projects

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

**Ready to revolutionize your AI development workflow?**

```bash
curl -sSL https://github.com/cosmic-hiker/morpheus-framework/raw/main/morpheus-setup.sh | bash
```

Then create your `.morpheus/brief.md` and start building with enhanced AI collaboration!
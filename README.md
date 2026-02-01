# College Helpdesk Agent

## Overview

A proof-of-concept agentic AI solution designed to streamline college support operations and improve student experience. This project was developed for the **IBM Dev Day AI Demystified Hackathon**.

## Problem Statement

Students and staff frequently face challenges accessing timely information about college procedures, policies, and administrative processes. Manual helpdesk operations are resource-intensive and often result in response delays. This solution leverages AI to provide instant, accurate responses to common queries while intelligently escalating complex issues to support teams.

## Solution

The **College Helpdesk Agent** is an intelligent conversational AI system that:

- **Answers Common Questions**: Provides immediate responses to frequently asked questions about exam fees, registration timelines, and other college policies
- **Smart Ticket Creation**: Automatically creates support tickets for complex issues like ID card complaints
- **Intelligent Escalation**: Routes non-standard queries to the appropriate support team for human intervention
- **24/7 Availability**: Provides round-the-clock support without requiring additional staff resources

## Key Features

✨ **Natural Language Processing** - Understands student queries in plain English  
✨ **Knowledge Base Integration** - Maintains an organized repository of college policies and procedures  
✨ **Automated Ticket Generation** - Creates support tickets with issue descriptions for escalation  
✨ **Context-Aware Responses** - Intelligently determines when to answer, escalate, or create tickets  
✨ **User-Friendly Interface** - Simple interactive command-line interface for easy access  

## Technology Stack

- **Language**: Python 3.x
- **Architecture**: Agentic AI with rule-based decision logic
- **Platform**: IBM watsonx Orchestrate (for production deployment)

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required for basic functionality

### Running the Application

```bash
python agent.py
```

The agent will start an interactive session. Simply type your questions and press Enter.

### Example Queries

```
Ask a question (type 'exit' to quit): What is the exam fee?
Agent: Undergraduate exam fee is $150 per exam.

Ask a question (type 'exit' to quit): When does semester registration start?
Agent: Semester registration opens in May and November.

Ask a question (type 'exit' to quit): I need to file an ID card complaint
Agent: Support ticket created successfully. Our support team will contact you via email.
```

## Project Structure

```
college-helpdesk-agent/
├── agent.py           # Main agent implementation
└── README.md          # Project documentation
```

## How It Works

1. **Query Input**: User submits a question through the interactive interface
2. **Processing**: Agent analyzes the query against its knowledge base
3. **Response Generation**: 
   - If a match is found → Immediate answer provided
   - If ticket-relevant (ID card, complaints) → Support ticket created
   - Otherwise → Query escalated to support team

## Judging Criteria Alignment

### ✅ Completeness & Feasibility (5 points)
- Fully functional proof-of-concept with clear implementation
- Demonstrates practical application of AI for college operations
- Clear pathway for integration with IBM watsonx Orchestrate

### ✅ Creativity & Innovation (5 points)
- Innovative approach to automate routine helpdesk operations
- Reduces manual workload while maintaining quality support
- Scalable architecture for expanding knowledge base and features

### ✅ Design & Usability (5 points)
- Simple, intuitive interface for students and staff
- Natural language interaction requires no technical knowledge
- Ready for immediate deployment across college departments

### ✅ Effectiveness & Efficiency (5 points)
- Addresses high-priority issue: reducing support response times
- Measurable impact: faster issue resolution and improved satisfaction
- Scalable: easily expands to handle more departments and query types

## Future Enhancements

- 🔄 Integration with college database for real-time information
- 💬 Multi-language support for diverse student populations
- 📊 Analytics dashboard for tracking common issues
- 📧 Email/SMS integration for ticket notifications
- 🧠 Machine learning for improved query classification
- 🔐 Role-based access control for different user types

## Hackathon Details

**Event**: IBM Dev Day AI Demystified Hackathon  
**Dates**: January 30 - February 1, 2026  
**Theme**: AI Demystified — From idea to deployment  
**Team**: College Helpdesk Team

## Getting Started for Judges

1. Clone or download this repository
2. Ensure Python 3.7+ is installed
3. Run `python agent.py`
4. Test with the example queries above
5. Type `exit` to quit the application

## Contact & Support

For questions about this project, please reach out to the development team.

---

**Status**: Proof-of-Concept ✓ | **Deployment Ready**: IBM watsonx Orchestrate Integration Pending


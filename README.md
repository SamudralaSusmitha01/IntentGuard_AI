# 🛡️ IntentGuard AI

### An Intent-Aware Multimodal AI Agent for Digital Distraction Detection and Adaptive Productivity Assistance

[![Project Status](https://img.shields.io/badge/Status-In%20Development-orange)](https://github.com/)
[![Project Type](https://img.shields.io/badge/Project-Major%20Project-blue)](https://github.com/)
[![Domain](https://img.shields.io/badge/Domain-Artificial%20Intelligence%20%26%20Machine%20Learning-purple)](https://github.com/)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React.js-61DAFB)](https://react.dev/)
[![License](https://img.shields.io/badge/License-To%20Be%20Decided-lightgrey)](LICENSE)

> **IntentGuard AI is an intelligent, context-aware productivity assistant that uses Multimodal Large Language Models (LLMs) and Agentic AI to understand user intentions, analyze digital activities, detect potential distractions, and provide personalized interventions that help users stay aligned with their goals.**

---

## 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Proposed Solution](#-proposed-solution)
4. [Project Objectives](#-project-objectives)
5. [Core Idea](#-core-idea)
6. [How the System Works](#-how-the-system-works)
7. [System Architecture](#-system-architecture)
8. [Complete Module Overview](#-complete-module-overview)
9. [Core AI Pipeline](#-core-ai-pipeline)
10. [Key Features](#-key-features)
11. [Online Product](#-online-product)
12. [Offline Product — Future Extension](#-offline-product--future-extension)
13. [Technology Stack](#-technology-stack)
14. [Project Structure](#-project-structure)
15. [Development Roadmap](#-development-roadmap)
16. [Research Contribution](#-research-contribution)
17. [Evaluation Strategy](#-evaluation-strategy)
18. [Privacy and Security](#-privacy-and-security)
19. [Team Responsibilities](#-team-responsibilities)
20. [Installation and Setup](#-installation-and-setup)
21. [Usage Workflow](#-usage-workflow)
22. [Project Status](#-project-status)
23. [Future Enhancements](#-future-enhancements)
24. [Expected Outcomes](#-expected-outcomes)
25. [Academic Information](#-academic-information)
26. [References](#-references)

---

# 🚀 Project Overview

## What is IntentGuard AI?

IntentGuard AI is a proposed AI-powered productivity assistant designed to help users maintain focus on their intended tasks while working on a computer.

The system begins by understanding the user's declared intention, such as:

* Study Machine Learning.
* Complete a programming assignment.
* Research Artificial Intelligence.
* Develop a React application.
* Prepare a project report.
* Read and understand a research paper.

During the focus session, the system analyzes relevant digital activity, including screen content, extracted text, active applications, browser context, and system events.

A multimodal AI reasoning engine compares the observed activity with the user's intended goal to determine whether the activity appears aligned or potentially distracting.

An agentic decision-making component then determines whether to take action, such as providing a gentle reminder, suggesting a return to the task, or taking no action.

The system is designed to maintain session history and user feedback so that intervention strategies can become more personalized over time.

### Main concept

```text
User Intention
      ↓
Digital Activity Understanding
      ↓
Intent–Activity Alignment
      ↓
Distraction Detection
      ↓
Adaptive AI Intervention
      ↓
User Feedback and Personalization
```

---

# 🎯 Problem Statement

The growth of digital technologies has improved access to information, communication, education, and productivity tools. However, users are also exposed to numerous digital distractions while working on computers.

Traditional productivity applications commonly rely on:

* Rule-based website blocking.
* Application blocking.
* Timer-based reminders.
* Manual task tracking.
* Fixed notification schedules.

These approaches do not necessarily understand the user's actual intention or the context of the activity being performed.

For example, a website such as YouTube can be used for:

* Watching an educational lecture.
* Learning Machine Learning.
* Following a programming tutorial.
* Watching unrelated entertainment.

A simple website blocker may treat all of these activities in the same way.

### The problem

> Existing productivity tools often lack the ability to understand the user's intended goal, interpret ongoing digital activity in context, and provide adaptive interventions based on the user's actual situation.

IntentGuard AI addresses this problem through intent-aware multimodal context analysis and agentic intervention.

---

# 💡 Proposed Solution

IntentGuard AI combines several AI and software engineering technologies into one integrated productivity system.

The proposed solution includes:

1. **AI-powered intention understanding**
2. **Focus-session management**
3. **Screen activity monitoring**
4. **Optical Character Recognition (OCR)**
5. **Active application detection**
6. **Browser context analysis**
7. **Multimodal AI reasoning**
8. **Intent–activity semantic alignment**
9. **Distraction detection**
10. **Temporal activity reasoning**
11. **Agentic intervention**
12. **User feedback**
13. **Session memory**
14. **Personalization**
15. **Productivity analytics**
16. **Online AI processing**
17. **Future offline AI processing**

The online product is the primary development target. Offline intelligence will be developed after the online product is complete.

---

# 🎯 Project Objectives

## Primary Objectives

### 1. Understand user intentions

Capture and interpret the user's intended task using an AI-powered intention understanding module.

### 2. Understand digital activity

Collect relevant contextual information from the user's digital environment.

### 3. Detect potential distractions

Compare the user's ongoing activity with their declared intention.

### 4. Provide adaptive interventions

Use an agentic decision-making system to generate context-aware and non-intrusive interventions.

### 5. Personalize the experience

Use session history and user feedback to improve future intervention strategies.

### 6. Build a complete AI product

Develop a full-stack system with a React frontend, FastAPI backend, database, AI services, monitoring, and analytics.

### 7. Evaluate the system

Measure the performance of the proposed approach through testing, baseline comparison, and ablation studies.

### 8. Develop offline capabilities later

Extend the system with locally runnable AI models and offline operation after the online product is stable.

---

# 🧠 Core Idea

## Intent–Activity Alignment

The central intelligence of IntentGuard AI is the comparison between:

> **What the user intends to accomplish**

and

> **What the user is currently doing**

### Example 1 — Focused Activity

**Declared intention:**

> Study Machine Learning and revise neural networks.

**Observed activity:**

* VS Code open.
* Neural network Python implementation.
* Relevant Machine Learning documentation.

**Expected interpretation:**

```text
Activity: Machine Learning development
Intent alignment: High
Status: Focused
```

### Example 2 — Potential Distraction

**Declared intention:**

> Complete a Machine Learning assignment.

**Observed activity:**

* Entertainment video.
* Unrelated social media browsing.
* Unrelated websites.

**Expected interpretation:**

```text
Activity: Unrelated entertainment
Intent alignment: Low
Status: Potentially distracted
```

### Example 3 — Legitimate Research

**Declared intention:**

> Build a RAG-based AI application.

**Observed activity:**

* Reading technical documentation.
* Searching for FastAPI implementation details.
* Reading a relevant research paper.

**Expected interpretation:**

```text
Activity: Technical research
Intent alignment: High
Status: Focused
```

### Important principle

> **The system should not classify an activity as distracting merely because of the application or website being used. It should consider the user's intention and the activity context.**

This is the foundation of the proposed system.

---

# ⚙️ How the System Works

## End-to-End Workflow

```text
┌───────────────────────────────┐
│          USER                 │
│                               │
│ "Study Machine Learning"      │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│     INTENT UNDERSTANDING      │
│                               │
│ Extract goal                  │
│ Identify expected activities  │
│ Refine user intention         │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       FOCUS SESSION           │
│                               │
│ Start / Pause / Resume / End  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│     DIGITAL MONITORING        │
│                               │
│ Screen capture                │
│ OCR                           │
│ Active application            │
│ Browser context               │
│ System events                 │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       CONTEXT BUILDER         │
│                               │
│ Combine all activity signals  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│    MULTIMODAL AI ANALYSIS     │
│                               │
│ Understand screen and context │
│ Compare with user intention   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│   INTENT–ACTIVITY ALIGNMENT   │
│                               │
│ Calculate contextual          │
│ relevance/alignment           │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│    DISTRACTION DETECTION      │
│                               │
│ Focused / Uncertain /         │
│ Potentially distracted        │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│    TEMPORAL REASONING         │
│                               │
│ Analyze activity over time    │
│ Avoid reacting to one event   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│   AGENTIC DECISION ENGINE     │
│                               │
│ Select appropriate action     │
└───────────────┬───────────────┘
                │
       ┌────────┴────────┐
       ▼                 ▼
┌──────────────┐  ┌──────────────┐
│ Intervention │  │  No Action   │
│ Notification  │  │              │
└──────┬───────┘  └──────────────┘
       │
       ▼
┌───────────────────────────────┐
│     USER FEEDBACK             │
│                               │
│ Helpful / Not helpful         │
│ Relevant / Taking a break     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      MEMORY & PERSONALIZATION │
│                               │
│ Store session history         │
│ Learn user preferences        │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       PRODUCTIVITY DASHBOARD  │
│                               │
│ Focus time                    │
│ Distraction events            │
│ Session history               │
│ Productivity analytics        │
└───────────────────────────────┘
```

---

# 🏗️ System Architecture

## High-Level Architecture

```text
                         ┌─────────────────────┐
                         │    REACT FRONTEND   │
                         │                     │
                         │  Home               │
                         │  Intent Input       │
                         │  Focus Session      │
                         │  Notifications      │
                         │  Dashboard          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    FASTAPI BACKEND  │
                         │                     │
                         │  REST APIs          │
                         │  Authentication     │
                         │  Session Management │
                         │  Service Layer      │
                         └──────────┬──────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ INTENT SERVICE  │       │ SESSION SERVICE │       │ USER SERVICE    │
│                 │       │                 │       │                 │
│ Goal extraction │       │ Start / Stop    │       │ Preferences     │
│ Refinement      │       │ Pause / Resume  │       │ Profile         │
└────────┬────────┘       └────────┬────────┘       └────────┬────────┘
         │                         │                         │
         └─────────────────────────┼─────────────────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │  MONITORING ENGINE  │
                         │                     │
                         │  Screen Capture     │
                         │  OCR                │
                         │  App Detection      │
                         │  Browser Context    │
                         │  System Events      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   CONTEXT BUILDER   │
                         │                     │
                         │  Unified Context    │
                         │  Data Validation    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      AI GATEWAY     │
                         │                     │
                         │  Model Abstraction  │
                         │  Provider Interface │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ MULTIMODAL AI MODEL │
                         │                     │
                         │  Context Analysis   │
                         │  Reasoning          │
                         │  Structured Output  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   INTELLIGENCE      │
                         │                     │
                         │  Alignment Engine   │
                         │  Distraction Model │
                         │  Temporal Reasoning │
                         │  Agentic Decisions  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  MEMORY & FEEDBACK  │
                         │                     │
                         │  Session History    │
                         │  User Feedback      │
                         │  Personalization    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       DATABASE      │
                         │                     │
                         │  PostgreSQL         │
                         │  SQLite (prototype) │
                         └─────────────────────┘
```

---

# 🔍 Complete Module Overview

## 1. Project Architecture

Defines the system structure, modules, interfaces, AI boundaries, data flow, repository organization, and development conventions.

### Responsibilities

* Design the complete architecture.
* Define module responsibilities.
* Define API boundaries.
* Define data flow.
* Select technologies.
* Establish development standards.

---

## 2. Database Module

Stores the data required by the system.

### Planned entities

```text
User
Intent
FocusSession
Activity
ContextAnalysis
Intervention
Feedback
SessionMetrics
```

### Responsibilities

* Store user information.
* Store declared intentions.
* Store focus sessions.
* Store activity records.
* Store AI analysis results.
* Store intervention history.
* Store feedback.
* Store productivity metrics.

---

## 3. React Frontend

Provides the user interface.

### Planned screens

* Home page.
* Intent input.
* Intent refinement.
* Focus session.
* Current activity.
* Intervention display.
* Session summary.
* Productivity dashboard.
* Settings and privacy controls.

### Responsibilities

* Capture user input.
* Display session state.
* Display AI-generated insights.
* Display interventions.
* Display analytics.
* Manage user interactions.

---

## 4. FastAPI Backend

Provides the backend application layer.

### Responsibilities

* Expose REST APIs.
* Manage users and sessions.
* Handle database operations.
* Coordinate AI services.
* Manage monitoring requests.
* Store analysis results.
* Deliver dashboard data.
* Manage system configuration.

---

## 5. Intent Understanding Module

Converts the user's natural-language intention into a structured representation.

### Example

Input:

> "I want to study Machine Learning and complete neural networks revision."

Expected structured representation:

```json
{
  "goal": "Study Machine Learning and revise neural networks",
  "category": "education",
  "expected_activities": [
    "Reading ML material",
    "Watching relevant lectures",
    "Writing ML code",
    "Taking notes",
    "Solving exercises"
  ],
  "potential_distractions": [
    "Unrelated entertainment",
    "Social media",
    "Gaming"
  ]
}
```

### Responsibilities

* Understand the user goal.
* Extract relevant activities.
* Identify potential distractions.
* Refine ambiguous intentions.
* Produce structured intent data.

---

## 6. Focus-Session Management

Manages the lifecycle of a user's focus session.

### Planned operations

```text
Create Session
      ↓
Start Session
      ↓
Pause Session
      ↓
Resume Session
      ↓
End Session
      ↓
Generate Summary
```

### Responsibilities

* Associate a session with an intention.
* Track start and end time.
* Track session status.
* Store session activities.
* Produce session metrics.

---

## 7. Screen Capture Module

Captures the user's screen during a focus session.

### Technology

PyAutoGUI.

### Responsibilities

* Capture screenshots.
* Associate captures with sessions.
* Add timestamps.
* Handle capture failures.
* Manage temporary image storage.
* Support privacy controls.

---

## 8. Active Application Detection

Identifies the active application and relevant window information.

### Example

```text
Application: VS Code
Window: neural_network.py
```

or:

```text
Application: Chrome
Window: YouTube
```

### Responsibilities

* Detect active application.
* Identify active window title.
* Record timestamps.
* Provide application context to the AI pipeline.

---

## 9. Browser Context Module

Collects relevant browser context where technically and ethically appropriate.

### Planned context

```text
Browser
URL / Domain
Page Title
Timestamp
```

### Responsibilities

* Collect browser context.
* Associate browser activity with sessions.
* Support contextual analysis.
* Respect user privacy and permissions.

---

## 10. OCR Module

Extracts text from screenshots.

### Technology

EasyOCR or Tesseract.

### Pipeline

```text
Screenshot
    ↓
OCR Engine
    ↓
Extracted Text
    ↓
Context Builder
```

### Responsibilities

* Extract visible text.
* Clean OCR output.
* Handle OCR errors.
* Associate text with screenshots.
* Provide text for semantic analysis.

---

## 11. Context Builder

Combines multiple signals into a unified representation.

### Example

```json
{
  "session_id": "session_001",
  "timestamp": "2026-01-01T10:00:00",
  "intent": {
    "goal": "Study Machine Learning",
    "category": "education"
  },
  "application": "Chrome",
  "window_title": "YouTube",
  "url": "youtube.com",
  "ocr_text": "Gradient Descent Neural Networks",
  "screenshot_reference": "capture_001"
}
```

### Responsibilities

* Combine monitoring signals.
* Validate input.
* Normalize data.
* Prepare AI requests.
* Preserve timestamps and session association.

---

## 12. Multimodal AI Analysis

The multimodal AI model analyzes screenshots and contextual information.

### Input

```text
User Intent
+
Structured Intent
+
Screenshot
+
OCR Text
+
Application
+
Browser Context
+
Session Context
```

### Expected output

```json
{
  "activity": "Watching a machine learning lecture",
  "category": "learning",
  "alignment": "aligned",
  "distraction_probability": 0.08,
  "confidence": 0.94,
  "reason": "The observed content is related to the declared goal."
}
```

These fields are proposed output design examples. Actual output schemas and thresholds will be finalized during implementation and evaluation.

---

## 13. Intent–Activity Alignment Engine

The central reasoning component.

### Purpose

Determine how closely the observed activity aligns with the user's intention.

### Conceptual inputs

```text
Intent
+
Activity
+
OCR
+
Application
+
Browser Context
+
Screenshot
+
Historical Context
```

### Conceptual output

```text
Alignment Score
Activity Category
Confidence
Reason
```

### Important consideration

The system should distinguish:

* Productive activity.
* Relevant research.
* Intentional breaks.
* Unrelated activity.
* Ambiguous activity.

The alignment mechanism must be evaluated rather than assumed to be accurate.

---

## 14. Distraction Detection Engine

Converts contextual analysis into a focus/distraction state.

### Planned states

```text
FOCUSED
PROBABLY_FOCUSED
UNCERTAIN
PROBABLY_DISTRACTED
DISTRACTED
```

### Responsibilities

* Interpret alignment.
* Consider confidence.
* Consider activity history.
* Identify possible distractions.
* Avoid unnecessary interruptions.
* Produce a structured classification.

---

## 15. Temporal Reasoning

Analyzes activity over time.

### Example

```text
10:00 → Machine Learning lecture
10:05 → Machine Learning lecture
10:10 → Unrelated video
10:15 → Unrelated video
10:20 → Unrelated browsing
```

The system can use a history-aware decision process rather than reacting to one isolated observation.

### Responsibilities

* Track recent activity.
* Identify persistent deviations.
* Reduce unnecessary reactions.
* Support session-level analysis.
* Improve intervention timing.

---

## 16. Agentic Intervention Engine

Determines what action should be taken after analyzing the user's context.

### Possible actions

```text
NO_ACTION
GENTLE_REMINDER
STRONGER_REMINDER
SUGGEST_BREAK
ASK_USER
```

### Decision inputs

```text
Current Intent
Current Context
Alignment
Distraction State
Duration
Historical Activity
Previous Interventions
User Preferences
Feedback
```

### Example

```text
Potential distraction detected
          ↓
Check severity
          ↓
Check duration
          ↓
Check previous interventions
          ↓
Check user preferences
          ↓
Choose appropriate action
```

The agent should be designed to avoid unnecessarily interrupting users.

---

## 17. User Feedback

Captures the user's response to interventions.

### Example

```text
Was this intervention helpful?

[ Yes ]
[ No ]
[ This was relevant ]
[ I was taking a break ]
```

### Responsibilities

* Collect feedback.
* Store intervention outcomes.
* Identify false interventions.
* Support personalization.
* Improve evaluation.

---

## 18. Session Memory

Stores the history of focus sessions.

### Example

```text
Session ID: 001

Goal:
Study Machine Learning

Total Session:
2h 14m

Focused:
1h 52m

Potential Distraction:
22m

Interventions:
3

Helpful Interventions:
2
```

### Responsibilities

* Store session history.
* Store activities.
* Store AI analyses.
* Store interventions.
* Store feedback.
* Support dashboard analytics.

---

## 19. Personalization

Uses user preferences and feedback to adapt the experience.

### Example

```text
User preference:
Gentle reminders

User feedback:
Frequent notifications are annoying

Future intervention:
Less frequent, more context-aware reminders
```

### Responsibilities

* Learn user preferences.
* Use intervention history.
* Adapt notification strategy.
* Improve future interactions.
* Preserve user control.

---

## 20. Real-Time Dashboard

Displays productivity and session information.

### Planned metrics

* Current focus state.
* Session duration.
* Focus duration.
* Potential distraction duration.
* Number of interventions.
* Intervention outcomes.
* Session history.
* Productivity trends.

### Planned views

```text
Today's Session
       ↓
Activity Timeline
       ↓
Focus Statistics
       ↓
Distraction Events
       ↓
Intervention History
       ↓
Personalized Insights
```

---

## 21. Privacy and Security

Privacy is a core consideration because the system processes screen activity and potentially sensitive digital information.

### Planned controls

* Monitoring ON/OFF.
* Screenshot capture ON/OFF.
* Browser monitoring ON/OFF.
* OCR processing ON/OFF.
* Session data deletion.
* Screenshot deletion.
* History clearing.
* Secure storage.
* User-controlled monitoring.

### Privacy principle

> Collect and retain only the information necessary for the intended functionality, with clear user control over monitoring and stored data.

The privacy implementation and retention policies will be finalized during development.

---

# 🤖 Core AI Pipeline

## AI Gateway

The AI gateway provides a common interface for model providers.

```text
                 AI GATEWAY
                     │
          ┌──────────┴──────────┐
          │                     │
      Cloud AI              Local AI
   (Online mode)         (Future mode)
          │                     │
          ▼                     ▼
   Gemini / OpenAI          Ollama /
   Provider                 Local Model
          │                     │
          └──────────┬──────────┘
                     ▼
             Common AI Output
                     │
                     ▼
          IntentGuard Intelligence
```

### Why use an AI gateway?

* Avoid hard-coding one provider.
* Simplify model replacement.
* Support experimentation.
* Enable future cloud/local routing.
* Keep the application architecture modular.

---

# 🌐 Online Product

## Primary Development Target

The online version will be built first.

### Planned online architecture

```text
React Frontend
      ↓
FastAPI Backend
      ↓
Intent Engine
      ↓
Session Management
      ↓
Monitoring Engine
      ↓
OCR + Context Builder
      ↓
Cloud Multimodal AI
      ↓
Alignment Engine
      ↓
Distraction Detection
      ↓
Agentic Intervention
      ↓
Memory + Feedback
      ↓
Dashboard
```

### Online product goals

* Complete focus-session workflow.
* AI-powered intent understanding.
* Digital activity monitoring.
* Multimodal context analysis.
* Distraction detection.
* Adaptive intervention.
* Session history.
* Productivity dashboard.
* Testing and evaluation.
* Stable online product architecture.

### Development cost strategy

The project will prioritize ₹0 development cost through:

* Open-source libraries.
* Free development tools.
* Local execution.
* Free/open-source databases.
* Free OCR.
* Free/local AI models wherever practical.
* Optional cloud AI usage only when available within a free quota or when explicitly chosen.

**No paid API or hosting service should be assumed as a mandatory dependency.**

---

# 📴 Offline Product — Future Extension

Offline development begins only after the online product is complete.

## Planned offline architecture

```text
              AI GATEWAY
                  │
         ┌────────┴────────┐
         │                 │
      ONLINE            OFFLINE
         │                 │
     Cloud AI          Local AI
         │                 │
         └────────┬────────┘
                  ▼
          Common AI Interface
                  │
                  ▼
           IntentGuard Engine
```

### Planned offline capabilities

* Local AI model execution.
* Local intent understanding.
* Local context analysis.
* Offline distraction detection.
* Offline intervention.
* Local session memory.
* Cloud/local routing.
* Local performance optimization.

### Possible technologies

* Ollama.
* ONNX Runtime.
* Lightweight local models.
* Local OCR.
* Local database.
* Model quantization.

The final model choices will depend on hardware compatibility, accuracy, latency, and evaluation results.

---

# 🛠️ Technology Stack

## Frontend

| Technology          | Purpose                        |
| ------------------- | ------------------------------ |
| React.js            | User interface                 |
| TypeScript          | Type-safe frontend development |
| Vite                | Frontend build tooling         |
| React Router        | Application routing            |
| CSS / UI components | Interface design               |

## Backend

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Primary development language |
| FastAPI    | Backend API framework        |
| Pydantic   | Data validation              |
| Uvicorn    | ASGI server                  |
| SQLAlchemy | Database ORM                 |

## AI / Machine Learning

| Technology                  | Purpose                      |
| --------------------------- | ---------------------------- |
| Multimodal LLMs             | Context reasoning            |
| Gemini / OpenAI             | Optional cloud AI providers  |
| Ollama                      | Future local model execution |
| Sentence Transformers       | Optional embeddings          |
| FAISS / other local storage | Optional semantic memory     |

## Computer Vision & Monitoring

| Technology                    | Purpose                      |
| ----------------------------- | ---------------------------- |
| PyAutoGUI                     | Screen capture               |
| EasyOCR                       | OCR                          |
| Tesseract                     | Alternative OCR              |
| OS-compatible libraries       | Active application detection |
| Browser-compatible approaches | Browser context              |

## Database

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| PostgreSQL | Primary database target             |
| SQLite     | Early prototype / local development |
| SQLAlchemy | Database access                     |

## Development & Deployment

| Technology                          | Purpose                   |
| ----------------------------------- | ------------------------- |
| Git                                 | Version control           |
| GitHub                              | Repository hosting        |
| Docker                              | Containerization          |
| Docker Compose                      | Local multi-service setup |
| Pytest                              | Backend testing           |
| Playwright / frontend testing tools | Frontend testing          |

---

# 📁 Project Structure

The following is the planned repository organization. It will be refined during Phase 01.

```text
intentguard-ai/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   ├── store/
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database/
│   │   ├── services/
│   │   ├── ai/
│   │   ├── agents/
│   │   ├── monitoring/
│   │   ├── context/
│   │   ├── memory/
│   │   └── analytics/
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── pyproject.toml
│
├── experiments/
│   ├── datasets/
│   ├── notebooks/
│   ├── baselines/
│   ├── ablations/
│   └── results/
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── research/
│   └── screenshots/
│
├── docker/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# 🗺️ Development Roadmap

## Layer 1 — Foundation

### Phase 01 — Project Architecture

Define the complete technical architecture, modules, data flow, APIs, AI boundaries, repository structure, and technology choices.

### Phase 02 — Database

Design and implement database schemas, models, relationships, migrations, and storage.

### Phase 03 — React Application

Build the frontend foundation, layouts, routing, components, and initial screens.

### Phase 04 — FastAPI Backend

Build the backend foundation, API structure, configuration, validation, database integration, and service architecture.

---

## Layer 2 — Perception & Context

### Phase 05 — Intent Understanding

Build the AI-powered intention capture, interpretation, refinement, and structured output.

### Phase 06 — Focus-Session Management

Implement session creation, starting, pausing, resuming, ending, and tracking.

### Phase 07 — Screen Capture

Implement screen capture using PyAutoGUI.

### Phase 08 — Active Application Detection

Detect active application and relevant window context.

### Phase 09 — Browser Context

Collect relevant browser context where appropriate.

### Phase 10 — OCR

Implement screenshot text extraction.

### Phase 11 — Context Builder

Combine intent, screenshot, OCR, application, browser, and timestamp information into a unified context.

---

## Layer 3 — AI Intelligence

### Phase 12 — Multimodal AI Analysis

Implement multimodal reasoning and structured AI outputs.

### Phase 13 — Intent–Activity Alignment

Develop the semantic alignment mechanism.

### Phase 14 — Distraction Detection

Build focus/distraction classification.

### Phase 15 — Temporal Reasoning

Introduce history-aware activity reasoning.

### Phase 16 — Agentic Intervention

Build the autonomous intervention decision engine.

---

## Layer 4 — Personalization & Product

### Phase 17 — User Feedback

Capture and process user responses.

### Phase 18 — Session Memory

Store session history and analysis results.

### Phase 19 — Personalization

Adapt interventions using preferences and feedback.

### Phase 20 — Real-Time Dashboard

Build the productivity dashboard and real-time session display.

### Phase 21 — Privacy & Security

Implement privacy controls, secure storage, data deletion, and monitoring permissions.

---

## Layer 5 — Research & Validation

### Phase 22 — Testing

Perform unit, integration, system, AI-pipeline, UI, and database testing.

### Phase 23 — Evaluation

Define datasets/scenarios, metrics, and experimental methodology.

### Phase 24 — Baseline Comparison

Compare the proposed approach against simpler methods.

### Phase 25 — Ablation Studies

Evaluate the contribution of individual components.

### Phase 26 — Online Product Complete

Finalize the online product, integration, testing, documentation, and research results.

---

## Layer 6 — Offline AI

### Phase 27 — Local AI

Introduce local AI models.

### Phase 28 — Cloud/Local AI Routing

Implement model/provider routing.

### Phase 29 — Offline Monitoring

Enable monitoring without internet connectivity.

### Phase 30 — Offline Reasoning

Implement local context analysis and distraction detection.

### Phase 31 — Offline Agentic Intervention

Enable local intervention decisions.

### Phase 32 — Offline Personalization & Memory

Support local history and personalization.

### Phase 33 — Online/Offline Integration

Integrate both modes through a common architecture.

### Phase 34 — Offline Optimization

Optimize local inference, latency, and resource usage.

### Phase 35 — Offline Evaluation

Compare online, offline, and hybrid performance.

### Phase 36 — Final IntentGuard AI

Finalize the complete integrated online/offline system.

---

# 🔬 Research Contribution

IntentGuard AI is designed to be more than a basic productivity application.

The research direction focuses on:

## 1. Intent-aware activity understanding

Understanding user activity relative to a declared goal.

## 2. Multimodal context analysis

Combining visual and contextual information to analyze digital activity.

## 3. Intent–Activity Semantic Alignment

Developing and evaluating a mechanism for comparing intention and observed activity.

## 4. Temporal distraction reasoning

Considering activity patterns over time rather than isolated events.

## 5. Agentic intervention

Selecting context-aware interventions based on activity, severity, history, and preferences.

## 6. Personalization

Using user feedback and history to adapt interventions.

## 7. Hybrid online/offline AI

Exploring cloud and local inference for availability, privacy, latency, and performance.

---

# 📊 Evaluation Strategy

Evaluation will be performed after the core system is implemented.

## 1. Intent Understanding Evaluation

Possible metrics:

* Intent extraction accuracy.
* Activity category accuracy.
* Structured output validity.

## 2. Distraction Detection Evaluation

Possible metrics:

* Accuracy.
* Precision.
* Recall.
* F1-score.
* Confusion matrix.

## 3. System Performance Evaluation

Possible metrics:

* Processing latency.
* End-to-end response time.
* OCR processing time.
* Model inference time.
* Resource usage.
* API usage where applicable.

## 4. Intervention Evaluation

Possible metrics:

* Intervention acceptance.
* Return-to-task rate.
* False intervention rate.
* Ignored interventions.
* User feedback.

## 5. Baseline Comparison

Potential baselines:

```text
Rule-Based Detection
        vs
OCR/Text-Based Analysis
        vs
LLM-Only Analysis
        vs
Proposed IntentGuard AI
```

The exact baselines and comparison methodology will be finalized during the research phases.

## 6. Ablation Studies

Potential experiments:

```text
Full System
      vs
Without OCR
      vs
Without Screenshot
      vs
Without Application Context
      vs
Without Browser Context
      vs
Without Temporal Reasoning
```

These experiments can help determine which contextual signals contribute to the system's performance.

---

# 🔐 Privacy and Security

IntentGuard AI deals with potentially sensitive digital activity.

The project therefore emphasizes:

* User-controlled monitoring.
* Explicit session activation.
* Data minimization.
* Secure storage.
* Screenshot lifecycle management.
* Deletion controls.
* Privacy-aware design.
* Transparent intervention behaviour.

### Important design principle

> The system should assist the user, not take away control from the user.

The project will avoid unnecessary collection of sensitive information and will make monitoring controls clear.

---

# 👥 Team Responsibilities

The project is being developed by a four-member team.

### Member 1 — AI/ML

Responsibilities:

* Intent understanding.
* Multimodal reasoning.
* Alignment engine.
* Distraction detection.
* AI evaluation.

### Member 2 — Monitoring & Computer Vision

Responsibilities:

* Screen capture.
* OCR.
* Active application detection.
* Browser context.
* Monitoring pipeline.

### Member 3 — Backend & Agent

Responsibilities:

* FastAPI.
* Database integration.
* Session management.
* Agentic decision engine.
* Memory services.

### Member 4 — Frontend & Product

Responsibilities:

* React application.
* User interface.
* Focus session screens.
* Dashboard.
* Notifications.
* User experience.

### Shared responsibilities

All members collaborate on:

* Integration.
* Testing.
* Research evaluation.
* Documentation.
* Project presentation.
* Final report.

---

# 🧪 Installation and Setup

> **Status:** Installation instructions will be finalized during Phase 01 and updated as development progresses.

## Prerequisites

Planned development environment:

* Python.
* Node.js and npm.
* Git.
* VS Code.
* PostgreSQL or SQLite.
* Docker (optional during early development).
* AI model/provider configuration.

## Clone the repository

```bash
git clone <repository-url>
cd intentguard-ai
```

## Backend setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

## Frontend setup

```bash
cd frontend

npm install

npm run dev
```

## Environment variables

A `.env.example` file will be provided.

Possible configuration:

```env
DATABASE_URL=
AI_PROVIDER=
AI_API_KEY=
BACKEND_URL=
```

Actual variables will be defined during implementation.

---

# 🖥️ Usage Workflow

The planned user workflow is:

### Step 1 — Open IntentGuard AI

Launch the frontend application.

### Step 2 — Declare intention

Enter a goal such as:

> "Complete my Machine Learning assignment."

### Step 3 — Refine intention

The AI interprets the goal and identifies expected activities.

### Step 4 — Start focus session

The user starts the session.

### Step 5 — Monitor activity

The system collects relevant digital context.

### Step 6 — Analyze context

The multimodal AI analyzes activity relative to the user's intention.

### Step 7 — Detect alignment

The system determines whether the activity appears aligned or potentially distracting.

### Step 8 — Agentic intervention

The system may provide a context-aware reminder or take no action.

### Step 9 — User feedback

The user can respond to the intervention.

### Step 10 — Session summary

The system displays session history and productivity analytics.

---

# 📌 Project Status

## Current Development Strategy

The project will be developed phase-by-phase.

### Online product

```text
Phase 01 → Phase 26
```

### Offline product

```text
Phase 27 → Phase 36
```

### Current status

* [ ] Phase 01 — Project Architecture
* [ ] Phase 02 — Database
* [ ] Phase 03 — React Application
* [ ] Phase 04 — FastAPI Backend
* [ ] Phase 05 — Intent Understanding
* [ ] Phase 06 — Focus-Session Management
* [ ] Phase 07 — Screen Capture
* [ ] Phase 08 — Active Application Detection
* [ ] Phase 09 — Browser Context
* [ ] Phase 10 — OCR
* [ ] Phase 11 — Context Builder
* [ ] Phase 12 — Multimodal AI Analysis
* [ ] Phase 13 — Intent–Activity Alignment
* [ ] Phase 14 — Distraction Detection
* [ ] Phase 15 — Temporal Reasoning
* [ ] Phase 16 — Agentic Intervention
* [ ] Phase 17 — User Feedback
* [ ] Phase 18 — Session Memory
* [ ] Phase 19 — Personalization
* [ ] Phase 20 — Real-Time Dashboard
* [ ] Phase 21 — Privacy & Security
* [ ] Phase 22 — Testing
* [ ] Phase 23 — Evaluation
* [ ] Phase 24 — Baseline Comparison
* [ ] Phase 25 — Ablation Studies
* [ ] Phase 26 — Online Product Complete

### Future offline development

* [ ] Phase 27 — Local AI
* [ ] Phase 28 — Cloud/Local AI Routing
* [ ] Phase 29 — Offline Monitoring
* [ ] Phase 30 — Offline Reasoning
* [ ] Phase 31 — Offline Agentic Intervention
* [ ] Phase 32 — Offline Personalization & Memory
* [ ] Phase 33 — Online/Offline Integration
* [ ] Phase 34 — Offline Optimization
* [ ] Phase 35 — Offline Evaluation
* [ ] Phase 36 — Final IntentGuard AI

---

# 🔮 Future Enhancements

Potential future extensions include:

* Improved multimodal reasoning.
* More accurate activity classification.
* Better personalization.
* More advanced temporal reasoning.
* Local AI models.
* Hybrid cloud/local inference.
* Better intervention policies.
* Privacy-preserving local processing.
* Improved analytics.
* Research publication.

These are planned possibilities, not guaranteed implemented features.

---

# 🎓 Expected Outcomes

The completed project is intended to provide:

1. A functional AI-powered productivity assistant.
2. An intent-aware activity analysis pipeline.
3. Multimodal context reasoning.
4. Distraction detection relative to user intention.
5. Adaptive agentic interventions.
6. Session memory and personalization.
7. Productivity analytics.
8. A modular online architecture.
9. A future path toward offline AI.
10. Experimental results supporting the system's design.

---

# 🏫 Academic Information

**Project Title:** IntentGuard AI

**Project Domain:** Artificial Intelligence and Machine Learning

**Project Type:** Major Project

**Batch ID:** AIML-C8

**Institution:** Vasireddy Venkatadri Institute of Technology (VVIT)

**Department:** CSE (AI)

**Team Size:** 4

**Development Approach:** Phase-by-phase implementation

**Primary Target:** Online IntentGuard AI

**Future Extension:** Offline and hybrid AI

---

# 📚 References

The following references are included in the submitted project abstract.

1. *State Your Intention to Steer Your Attention: An AI Assistant for Intentional Digital Living.*
   [arXiv](https://arxiv.org/abs/2510.14513)

2. *The Invisible Mentor: Inferring User Actions from Screen Recordings to Recommend Better Workflows.*
   [arXiv](https://arxiv.org/abs/2509.26557)

3. *Proactive Visual Analytics with LLM-Based UI Agents (ProactiveVA).*
   [IEEE Xplore](https://ieeexplore.ieee.org/document/11011093)

4. *From Gaze to Guidance: Interpreting and Adapting to Users' Cognitive Needs with Multimodal Gaze-Aware AI Assistants.*
   [Microsoft Research](https://www.microsoft.com/en-us/research/publication/from-gaze-to-guidance-interpreting-and-adapting-to-users-cognitive-needs-with-multimodal-gaze-aware-ai-assistants/)

5. *Students' Attention Monitoring System in Learning Environments Based on Artificial Intelligence.*
   [IEEE Xplore](https://ieeexplore.ieee.org/document/9662181)

6. *Application of Machine Learning and Image Recognition for Driver Attention Monitoring.*
   [IEEE Xplore](https://ieeexplore.ieee.org/document/10187230)

7. *Deep Learning-Based Real-Time Driver Cognitive Distraction Detection.*
   [IEEE Xplore](https://ieeexplore.ieee.org/document/10876120)

8. *A Real-Time, Privacy-Preserving Approach for Cognitive Strain Detection Using Micro-Temporal Eye Behavior.*
   [IEEE Xplore](https://ieeexplore.ieee.org/document/11489437)

9. *Trust in AI and Its Role in the Acceptance of AI Technologies.*
   [arXiv](https://arxiv.org/abs/2203.12687)

---

## ⭐ Project Vision

> **IntentGuard AI aims to make digital productivity more intentional by understanding what users want to accomplish, interpreting their digital activities, and helping them stay aligned with their goals through intelligent, adaptive, and privacy-aware AI assistance.**

---

### Development Philosophy

**Build carefully. Test every module. Document every phase. Evaluate every important claim.**

The project will be developed one phase at a time, beginning with the online product and extending to offline AI after the online system is complete.

---

**IntentGuard AI — Building an Intelligent Assistant for Intentional Digital Productivity.**

# Basic Calculator
A robust, modern, full-stack mathematical calculator built with flask and python's `ast` module. The application replaces `eval` implementations with a custom ast evaluator, offers regex-based implicit mulltiplication preprocessing, maintains session-isolated calculation memory and delivers a responsive, dark-themed interactive UI.

---

## Table of Contents
- [Overview] (#overview)
- [Key Features] (#key-features)
- 

---

# Overview
The **Calculator** transitions traditional command-line calculator logic into a secure, browser-accessible web service.

The backend prioritizes input validation, mathematical correctness and defense-in-depth security by eliminating arbitrary code execution vectors typically introduced by `eval()`.

---

## Key Features
- **Safe AST Evaluation Engine**: Parses expressions into python abstract syntax trees to ensure only mathematical expressions, constants and whitelisted functions execute.

-- **Natural Language Preprocessing:** Pre-processes natural mathematical expressions with regular expressions to support implicit multiplication.

--**Session Isolated Memory:** 
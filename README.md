# Cryptographic Cipher with Keylogger 🔐

## Overview
This project demonstrates simple text obfuscation combined with a **consensual input-capture simulation** for learning purposes. The cryptographic component illustrates a basic ROT13 transformation plus an extra reversible obfuscation layer. The “keylogger” aspect is represented only as a safe, simulated input log (for example, a pre-recorded text file) so you can study how logging and reversible obfuscation might work in a controlled lab environment.

This repository is intended for:
- Learning about reversible text transformations and the limits of simple ciphers (ROT13 + lightweight obfuscation).  
- Demonstrating how captured input (with explicit consent) can be stored and later obfuscated/deobfuscated.  
- Discussing ethics, defensive measures, and how to detect/mitigate unauthorized logging.

## What it contains (high-level)
- A reversible ROT13-based obfuscator with an additional special-character layer to increase readability of the demo output.  
- Scripts that accept **local files** (simulated input logs) and perform encode/decode operations.  
- Clear ethical guidance and safe usage examples that use only local files you own.

> No code or instructions for stealthy key capture (system-wide hooks, background services, or malware techniques) are provided.

## Features (educational)
- **ROT13 transformation:** Classic letter-substitution for easy reversible demonstration.  
- **Extra obfuscation:** Deterministic insertion or transformation of special characters to illustrate layered transformations that are still reversible.  
- **Simulated input logs only:** Demonstrations operate on files you provide (e.g., `sample_input_log.txt`) — never on other people’s devices or accounts without consent.  
- **Decode/Recover:** Full round-trip demonstration to show how reversible obfuscation works.


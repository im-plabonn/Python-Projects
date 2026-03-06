# Password Strength Checker

A lightweight and efficient password strength evaluation tool built using Python and Gradio.



## Overview
This application analyzes password security based on character composition and length. It provides immediate feedback by assigning a score from 0 to 5.

## Security Criteria
The tool evaluates the password based on these five factors:
1. **Length:** Minimum 8 characters.
2. **Uppercase:** Contains at least one uppercase letter (A-Z).
3. **Lowercase:** Contains at least one lowercase letter (a-z).
4. **Digit:** Contains at least one number (0-9).
5. **Special Characters:** Contains at least one symbol (@, #, $, etc.).

## Evaluation Levels
- **Weak (🔴):** Score ≤ 2
- **Medium (🟡):** Score 3 - 4
- **Strong (🟢):** Score 5

## Prerequisites
Ensure you have Python installed. You will need the Gradio library to run the interface.

```bash
pip install gradio
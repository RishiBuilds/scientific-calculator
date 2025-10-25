# Scientific Calculator with History Log and Theme Toggle

## Project Description
This project is a full-featured scientific calculator built with Python and Tkinter. It provides both basic arithmetic operations and advanced scientific functions with an elegant user interface that includes a history log and dark/light mode toggle.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [Implementation Details](#implementation-details)
8. [Workflow Diagram](#workflow-diagram)
9. [Future Work](#future-work)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction
This calculator application was designed to provide a comprehensive yet user-friendly tool for performing mathematical calculations. It combines the simplicity of a basic calculator with the power of scientific functions, all wrapped in a modern and customizable interface.

## Features
### Basic Operations
- Arithmetic operations (addition, subtraction, multiplication, division, percentage)
- Decimal and integer calculations
- Clear Entry (CE) and Clear All (C) functions
- Backspace support

### Scientific Functions
- Trigonometric functions: sin, cos, tan, asin, acos, atan
- Logarithmic functions: log (base 10), ln (natural log)
- Powers and roots: square root, x², x³, xⁿ
- Factorial (!)
- Inverse (1/x)
- Mathematical constants: π (pi), e (Euler's number)

### Advanced Features
- **Memory Functions**: MC (Memory Clear), MR (Memory Recall), M+ (Memory Add), M- (Memory Subtract)
- Interactive history log with clear history feature
- Dark/Light theme toggle for user preference
- Sign toggle (positive/negative)
- Professional color scheme with vibrant buttons
- Error handling for invalid expressions
- Keyboard input support for efficient calculations
- Modern UI with smooth transitions

## Technologies Used
- Python 3.13
- Tkinter (GUI library)
- Math module for scientific operations
- Object-Oriented Programming principles

## Installation
To run this calculator application, ensure you have Python installed on your system:

```bash
# Clone the repository (if applicable)
git clone https://github.com/RishiBuilds/scientific-calculator.git

# Navigate to the project directory
cd scientific-calculator

# Run the application
python main.py
```

No additional dependencies are required as Tkinter is included in standard Python installations.

## Usage
1. **Basic Operations**: Click on the digit buttons and operators to build expressions
2. **Scientific Functions**: Use sin, cos, tan, log, asin, acos, etc. for advanced calculations
3. **Memory Functions**: 
   - **MC**: Clear memory
   - **MR**: Recall stored value
   - **M+**: Add current value to memory
   - **M-**: Subtract current value from memory
4. **History**: Review past calculations in the history panel on the left (use 🗑️ to clear)
5. **Theme Toggle**: Switch between dark and light modes using the toggle button
6. **Clear Functions**:
   - **C**: Clear all (resets calculator)
   - **CE**: Clear entry (clears current input only)
   - **⌫**: Backspace (deletes last character)
7. **Special Functions**:
   - **±**: Toggle positive/negative
   - **1/x**: Calculate reciprocal
   - **!**: Factorial
   - **x², x³**: Square and cube operations
8. **Keyboard Input**: Use your keyboard for faster input:
   - Number keys (0-9) for digits
   - Standard operators (+, -, *, /)
   - Enter key to evaluate expressions
   - Backspace to delete last character
   - Escape key to clear the expression
   - Keyboard shortcuts for functions: 's' for sin, 'c' for cos, etc.

### Example Operations:
- Basic arithmetic: `5 + 7 = 12`
- Using constants: `2 × π = 6.28318...`
- Scientific functions: `sin(π/2) = 1`
- Powers: `2^8 = 256` or `5² = 25`
- Factorial: `5! = 120`
- Combined operations: `3 × (4 + 5) = 27`
- Inverse: `1/4 = 0.25`
- Inverse trigonometric: `asin(0.5) = 0.524`

## Screenshots
![Dark Mode](assets/dark_mode.png)
![Light Mode](assets/light_mode.png)

## Implementation Details
The calculator is implemented using object-oriented programming with the following key components:

- **Main Application Class**: Manages the overall application state and UI
- **Display System**: Shows the current expression and calculation results
- **Button Grid**: Organized layout for digits, operators, and functions
- **Calculation Engine**: Evaluates mathematical expressions safely
- **History System**: Records and displays calculation history
- **Theme Manager**: Handles switching between dark and light color schemes
- **Keyboard Handler**: Processes keyboard events for direct input

## Workflow Diagram

Below is a diagram illustrating the workflow of the calculator application:

```mermaid
flowchart TD
    A[User Input] -->|Button Click/Keyboard Press| B[Input Handler]
    B --> C{Input Type?}
    C -->|Number/Operator| D[Add to Expression]
    C -->|Function| E[Add Function to Expression]
    C -->|Equals| F[Evaluate Expression]
    C -->|Clear/Delete| G[Modify Expression]
    C -->|Theme Toggle| H[Switch Theme]
    D --> I[Update Display]
    E --> I
    F --> J[Process Calculation]
    J --> K[Format Result]
    K --> L[Update History]
    L --> I
    G --> I
    H --> M[Apply Theme Settings]
    M --> I
```

## Future Work
- Implement unit conversion capabilities
- Ability to save calculation history to a file
- Add scientific notation support
- Implement bracket matching and syntax highlighting
- Create a mobile-friendly responsive design
- Add graphing capabilities
- Support for complex numbers

## Contributing
Contributions to improve the calculator are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/rishichaurasia/scientific-calculator?tab=MIT-1-ov-file#) file for details.

## Author
**Rishi Chaurasia** - Developer of this Scientific Calculator

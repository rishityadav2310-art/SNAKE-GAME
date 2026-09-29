# Problem Statement & Objective

## Objective
Develop a lightweight, functional 2D Snake game in Python applying Object-Oriented Programming (OOP) principles and modular architecture.

## Problem Context
Snake is a classic arcade game where the player maneuvers a growing line/snake within a bounded field. The primary challenges addressed in this implementation are:

1. **Game Loop Mechanics**: Managing tick rates (turn timing) to control snake movement speed smoothly using event scheduling (`after` callbacks in Tkinter).
2. **State Management**: Accurately tracking coordinates for the snake's head and body segments to handle collision detection (walls and self) and growth mechanisms.
3. **Control Constraints**: Preventing illegal direction changes (e.g., immediate 180-degree turns that cause self-collisions).

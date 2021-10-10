## Requirements engineering
All information about requirements can be found in the following file: [link](https://docs.google.com/document/d/1YJfG6R8hqVHXyAWbUEWD7GAZxAxY5GQK/edit#)

## Glossary
All the used terminology can be found on the same [link](https://docs.google.com/document/d/1YJfG6R8hqVHXyAWbUEWD7GAZxAxY5GQK/edit#) at the end of the file.

## Architecture
For easier description of our architecture, we made two diagrams:
* **Static View diagram**  
![Static View](/Documentation/static_view.png)
* **Dynamic View diagram**  
![Dynamic View](/Documentation/dynamic_view.png)

## Design
* This **Sequence Diagram** shows how our app is going to interact with the user and with itself internally.  
![Sequence Diagram](/Documentation/sequence.jpg)
* About the designing of the classes itself (also called **Design Patterns**), we desided not to invent anything new, and just build our code around default **PyQt** code style. Interaction between any two classes is made either by **PyQt** itself, or by **signals**, taken from the same **PyQt** library.

## SOLID
* We tried our best to follow all the SOLID principles in our code. For better explanation of why we structured our code the way we did it, read documentation, which is right in the code. There we fully explained why each of our classes fits perfectly all the SOLID principles.
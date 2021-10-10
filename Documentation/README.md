## Requirements engineering
All information about requirements can be found in the following file: [link](https://docs.google.com/document/d/1YJfG6R8hqVHXyAWbUEWD7GAZxAxY5GQK/edit#)

## Glossary
All the used terminology can be found on the same [link](https://docs.google.com/document/d/1YJfG6R8hqVHXyAWbUEWD7GAZxAxY5GQK/edit#) at the end of the file.

## Architecture
For easier description of our architecture, we made the following diagrams:
* **UML Class Diagram**
![UML Classes](/Documentation/class_diagram.png)
* **Static View diagram**  
![Static View](/Documentation/static_view.png)
* **Dynamic View diagram**  
![Dynamic View](/Documentation/dynamic_view.png)
## Design
* This **Sequence Diagram** shows how our app is going to interact with the user and with itself internally.  
![Sequence Diagram](/Documentation/sequence.jpg)
* We used **Visitor** pattern for widget handlers (see [code](../Avaday/Handlers/widget_handlers.py)). They operate on data from data handlers (see [code](../Avaday/Handlers/data_handlers.py)). * Most of our classes inherit from **PyQt** classes. **PyQt** uses signals and slots for calling other classes' methods. We used **Mediator** pattern in ImageUpdater (see [code](../Avaday/Handlers/widget_handlers.py)) to re-transmit signals from view space to output image widget.
* We do not have child classes for any of our custom class, so several SOLID principles like L,I,D hardly apply to them.

## SOLID
* We did our best to follow SOLID principles in our code. To make our explanation more visual we give arguments on why we consider each our class SOLID-compliant right in the code. Please, confer classes in [Handlers](../Avaday/Handlers) or [Widgets](../Avaday/Widgets) to read our explanations.

## Linter results
* To prove, that our code is well-written, we checked our code using external service **SonarCloud**. It's report:  
![SonarCloud Report](/Documentation/sonarcloud_report.png)

## Tests 
* We used manual UI tests
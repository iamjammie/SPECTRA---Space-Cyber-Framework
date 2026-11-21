# Playbook: Assess an attack path

Related techniques: Any path in the navigator.

Use in an exercise first. Adapt to your mission's procedures and authority before relying on it.

## Steps

1. Open the path in Attack paths and select Show this path on the matrix.
2. Confirm written authorisation, environment and stop conditions for every step.
3. For each technique in order, check the precondition. If it cannot hold, mark Not applicable and say why.
4. Run the minimum action that answers the assessment question.
5. Capture the evidence named by the technique.
6. Note the first control that stopped or detected the step.
7. If the step succeeded, continue to the next; if it was broken, record the state reached and stop.
8. Run the recovery test for the last technique reached.
9. Set status and notes per technique in Assessment and export the file.
10. Raise an engineering action for each Exposed technique with an owner and date.

## Measure

- State at which the path broke
- Time to detect and respond
- Recovery time to an attested state

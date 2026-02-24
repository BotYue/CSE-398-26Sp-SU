# Week 7 Wed: LLM

---------------
#### :dizzy: **Lab Date :** Feb 23
#### :alarm_clock: **Due Date :** 2:00 pm Mar 2   
#### :pencil: Every group member must be present for every check point.
-------------------

## 0. Preparation

- [ ] Choose any api-based LLM on your preference, such as Open AI, Gemini, Claude, ...

- [ ] Create 2 api keys: one key for Task 1.. Text-based Input
You don't need to show the api key in the Markdown submission.

- [ ] The Task today is to develop an **EE Circuit tutor** for students.

- [ ] We have prepared materials in course GitHub repo "Regular Lab Phase -> Asset".
	There are 10 circuits in total. Each circuit is represented by 2 formats:
	* SPICE (text based format)
	* Image (screenshot from LTSpice software)

- [ ] The circuits are from the open-access textbook: *"Circuit Analysis and Design, 3rd Edition, Umich Publication"* https://services.publishing.umich.edu/Books/Electrical-Engineering-Textbooks

- [ ] There is no depedent sources in all the given circuits. Circuits solutions are given in the BlackBoard for references.




------

## 1. Text-based Input

- [ ] Use an LLM model, create a system that:

* Accepts a SPICE-format netlist input.
* Performs **Nodal Analysis** with correct math.
* Provide structured, student-understandable text output that clearly explains the solving procedure.

- [ ] For the Markdown submission, provide the full code. If your prompt is stored in a separate file, explicitly show it.
- [ ] For the Markdown submission, you only need to include **2 LLM outputs of the 10 circuits**.

- [ ] Create a Markdown table to report:

  * The **final nodal solution** (final node voltages)
  * Whether it is **Correct** compared with the official solutions (BlackBoard)

| Circuit # | Final node voltages (V) | correct? (Y/N) | Mismatch reason if |
| --------: | ---------------------------------------- | :----------------------: | ---------------------------- |
|         1 | V(n1)=...; V(n2)=...          |           Y / N          |  ---------------------------- | 
|         ... | ...      |         ...       |  ... | 

* [ ] **Accuracy calculation (all 10 circuits):**
  Evaluate correctness for all 10 circuits, then compute:

$$\text{Accuracy} =\frac{\text{Correct circuits}}{10}\times $$



> If can also correctly perform **Mesh Analysis** 
>
> can get **3/20 extra points back** in one single previous Markdown submission. (reach out to TA to recover your points)


-------

## 2. Image-based Input





🎉 **Check Point 2**

Each student must present **individually for 30 seconds** to describe personal contributions during this lab.<br>
Each student will be asked a question.<br>
The other two students in the same group must not assist.<br>
Failure to demonstrate meaningful contribution, or answer questions will result in point loss in the corresponding Markdown submission.

import subprocess   

user_task = "create a file name hello.txt with the word himalaya inside"

prompt = f"""
you are a helpful coding agent
if the user gives you a task, you will respond with a command
 to run in the shell to complete the task. you must respond with a command in the following format:
<tool=run_shell>your command here</tool>
dont explain yourself. just output the tool call
user task: {user_task}

"""

max_turn = 10
history = []
current_turn = 0

while current_turn < max_turn:
    current_turn += 1
    print(f"Turn {current_turn}:")


# The Brain
    print("Prompting the LLM...")
    ollama_result = subprocess.run(
        ["ollama", "run", "qwen2.5-coder:3b", prompt],
        capture_output=True,
        text=True
    )


    llm_response = ollama_result.stdout
    print(f"LLM Response: {llm_response}")


    # extraction logic
    start_tag = "<tool=run_shell>"
    end_tag = "</tool>"

    start_index = llm_response.find(start_tag)

    if start_index != -1:
        end_index = llm_response.find(end_tag, start_index)
        if end_index != -1:
            command = llm_response[start_index + len(start_tag):end_index].strip()
            print(f"Executing command: {command}")

            # Execution and observation
            a = subprocess.run(command, shell=True,capture_output=True, text=True)
            result = a.stdout.strip() if a.stdout else a.stderr.strip()
            print(f"Command output: {result}")

            print("Command executed.")
        else:
            print("End tag not found in the response.")
    else:
        print("No tool command found in the response.")

        


    




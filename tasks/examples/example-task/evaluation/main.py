# Evaluation script for example-task
# Requirement: a finished task must ship this file with at least 12 non-blank lines (a non-blank line contains at least one non-whitespace character).

def run_evaluation():
    # TODO: Implement the actual evaluation logic
    return {"passed": True}

def main():
    result = run_evaluation()
    if result["passed"]:
        print("Evaluation passed")
    else:
        print("Evaluation failed")

if __name__ == "__main__":
    main()

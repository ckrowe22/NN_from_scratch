import pydocstyle

results = pydocstyle.check(["DoublyLinkedList.py"])
errors = 0
for line in results:
    print(line)
    errors += 1
exit(errors)
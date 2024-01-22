import pydocstyle

results = pydocstyle.check(["NNData.py"])
errors = 0
for line in results:
    print(line)
    errors += 1
exit(errors)
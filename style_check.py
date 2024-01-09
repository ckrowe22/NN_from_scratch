import pycodestyle

style = pycodestyle.StyleGuide()
result = style.check_files(['DoublyLinkedList.py'])
if result.total_errors > 0:
    print(f"The following PEP-8 violations were flagged:")
    print(f"Line\tError\n")
for item in result._deferred_print:
    print(f"{item[0]}\t{item[2]} - {item[3]}\n")
exit(result.total_errors)

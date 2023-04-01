from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["a", "b", "c"])
table.add_column("Type Name", ["a", "b", "c"])
table.align = "l"
print(table)
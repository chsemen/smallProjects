import ezsheets

ss = ezsheets.createSpreadsheet('Delete me')

print(ezsheets.listSpreadsheets())
# ss.delete()
ss.delete(permanent=True)
print(ezsheets.listSpreadsheets())
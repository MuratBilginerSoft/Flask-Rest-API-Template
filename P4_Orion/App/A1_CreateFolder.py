import os

migrationFolderList = ["P4_Orion/migrations", "P4_Orion/migrationsPro"]

for folder in migrationFolderList:
    if not os.path.exists(folder):
        os.makedirs(folder)


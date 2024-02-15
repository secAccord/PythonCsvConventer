import os
def list_csv_files(directory):

  files = []
  for file in os.listdir(directory):
    if file.endswith(".csv"):
      files.append(file)
  return files


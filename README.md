# renamer
Iterations on the Seed Renamer job for testing with Scale

## Classic Renamer
This is the classic file renamer job. This job takes two arguments (INPUT_FILE and OUTPUT_DIR), renames the INPUT_FILE to <INPUT_FILE_NAME>_RENAMED.<extension> and saves it to the specified OUTPUT_DIR. 
  
To build the Seed image:
Use the [Seed CLI](https://github.com/ngageoint/seed-cli) and run `seed build`. The Seed CLI will pull the job name and version from the seed manifest. The resulting Docker image will be called `renamer-seed-1.0.0:1.0.0`.

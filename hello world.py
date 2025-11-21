chsh -s /bin/zsh
print("hello world")
# --- Configure Git identity (REQUIRED) ---
git config --global user.name "mine607gem"
git config --global user.email "heathsullivanpatti@gmail.com"

# --- Initialize repo (safe even if already initialized) ---
git init

# --- Set GitHub remote (replace USERNAME) ---
git remote remove origin 2> /dev/null
git remote add origin https://github.com/USERNAME/DogTracker.git

# --- Create or switch to main branch ---
git checkout -b main 2> /dev/null || git checkout main

# --- Stage all files (including HelloWorld.py) ---
git add .

# --- Commit ---
git commit -m "Add HelloWorld.py"

# --- Push to GitHub ---
git push -u origin main


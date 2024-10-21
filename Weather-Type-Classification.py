from huggingface_hub import HfApi
api = HfApi()
api.create_repo("Karan1908/Weather-Type-Classification", exist_ok=True)

from huggingface_hub import HfApi, Repository

# Variables for your username and model repo name
username = "Karan1908"  # Replace with your actual Hugging Face username
model_name = "Weather-Type-Classification"  # Name of the model repo you want to create/upload to

# Create the full repo name
repo_name = f"{username}/{model_name}"

# Local directory where your model files are located
local_dir = "/home/karan-chauhan/WorkStation/Project/Project"  # Replace with your model directory

# Initialize repository object and clone the repo
repo = Repository(local_dir=local_dir, clone_from=repo_name)

# Add all files in the directory and commit the changes
repo.push_to_hub(commit_message="Initial model upload")

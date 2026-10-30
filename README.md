## How to set up the environment

1. Open your terminal and navigate to the root directory containing the `pyproject.toml` file.
2. Run the sync command:
   ```bash
   uv sync
   ```
   It checks the `pyproject.toml` file, creates a virtual environment (`.venv`) if one does not exist, updates the `uv.lock` file, and installs all listed packages.
3. Navigate to the `notebooks` folder.
4. Rename the `.env_copy` file to `.env` and add your API keys for OpenAI, Gemini, and any other services you plan to use.

Set `SUPERMEMORY_NAMESPACE` in that `.env` file to choose the Supermemory container tag used by this deployment. It defaults to `loan_applicants` for existing setups. Applicant IDs are also applied as metadata filters and checked on returned memories to prevent cross-applicant retrieval.